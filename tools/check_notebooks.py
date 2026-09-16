"""Execute every notebook and report cells that fail or warn.

Usage (from the repository root):

    python tools/check_notebooks.py                 # all notebooks
    python tools/check_notebooks.py path/to/nb.ipynb [more.ipynb ...]
    python tools/check_notebooks.py --save exercises/solutions/06_SOL_*.ipynb

With --save, the executed notebook is written back with its outputs (skipped
cells get empty outputs). Use this for the solution notebooks, which are
committed with outputs; teaching and exercise notebooks are committed without.

Every notebook is run from top to bottom in a fresh kernel, with its own folder
as the working directory (so relative paths such as ../data/alice.txt behave as
they do for a student). Cells are handled according to their tags:

    raises-on-purpose   an exception is expected; reported if the cell succeeds
    needs-input         skipped (the cell calls input())
    skip-check          skipped

Any other cell that raises, or that prints a Warning to stderr, is reported.
Files that a notebook creates while running are deleted afterwards, and the
notebooks themselves are never modified.

Exit status is 1 when at least one problem was found, so the script can be
used in a pre-push check.
"""

import os
import re
import sys
import glob
import shutil
import tempfile

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import NOTEBOOK_DIRS, TAG_RAISES, TAG_INPUT, TAG_SKIP  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TIMEOUT = 300  # seconds per cell
SCHEDULE_WORDS = re.compile(r"\b(this (morning|afternoon)|(next|last) week|on (Mon|Tues|Wednes|Thurs|Fri)day|tomorrow|yesterday)\b", re.I)


def snapshot(folder):
    """Set of (path, mtime) for everything under folder, to detect files written by a notebook."""
    seen = {}
    for dirpath, _, files in os.walk(folder):
        for f in files:
            p = os.path.join(dirpath, f)
            seen[p] = os.path.getmtime(p)
    return seen


def check(path, save=False):
    nb = nbformat.read(path, as_version=4)
    folder = os.path.dirname(os.path.abspath(path))

    # Replace the source of cells we must not run by a no-op, remembering what we did.
    skipped, expected_errors, sources = [], set(), {}
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        tags = set(cell.get("metadata", {}).get("tags", []))
        if tags & {TAG_INPUT, TAG_SKIP}:
            sources[i] = cell.source
            cell.source = ""
            cell.outputs = []
            skipped.append(i)
        elif TAG_RAISES in tags:
            expected_errors.add(i)

    before = snapshot(folder)
    before_data = snapshot(os.path.join(ROOT, "data"))
    client = NotebookClient(nb, timeout=TIMEOUT, kernel_name="python3",
                            allow_errors=True, resources={"metadata": {"path": folder}})
    problems = []
    try:
        client.execute()
    except Exception as e:  # kernel died, timeout, ...
        problems.append(f"execution aborted: {e!r}"[:300])

    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        errors = [o for o in cell.get("outputs", []) if o.get("output_type") == "error"]
        warnings = [o for o in cell.get("outputs", [])
                    if o.get("output_type") == "stream" and o.get("name") == "stderr"
                    and "Warning" in "".join(o.get("text", ""))]
        first_line = "".join(cell.source).strip().split("\n")[0][:70]
        if i in expected_errors:
            if not errors:
                problems.append(f"cell {i}: tagged {TAG_RAISES} but ran without error | {first_line}")
            continue
        for o in errors:
            problems.append(f"cell {i}: {o['ename']}: {o['evalue'][:120]} | {first_line}")
        for o in warnings:
            text = "".join(o["text"]).strip().split("\n")[0][:160]
            problems.append(f"cell {i}: warning: {text} | {first_line}")

    # Style: no schedule-relative references outside the generated header cell.
    for i, cell in enumerate(nb.cells[1:], start=1):
        if cell.cell_type != "markdown":
            continue
        m = SCHEDULE_WORDS.search(cell.source)
        if m:
            problems.append(f"cell {i}: schedule-relative phrase {m.group(0)!r}; refer to sessions by topic instead")

    if save:
        for i, src in sources.items():
            nb.cells[i].source = src
            nb.cells[i].outputs = []
            nb.cells[i].execution_count = None
        nbformat.write(nb, path)

    # Remove anything the notebook wrote, restore anything it modified in data/ (best effort).
    for folder_, old in ((folder, before), (os.path.join(ROOT, "data"), before_data)):
        for p, mtime in snapshot(folder_).items():
            if p not in old:
                os.remove(p)
            elif old[p] != mtime and os.path.abspath(p) != os.path.abspath(path):
                problems.append(f"modified an existing file: {os.path.relpath(p, ROOT)}")
    return problems, skipped


def main(argv):
    save = "--save" in argv
    argv = [a for a in argv if a != "--save"]
    if argv:
        paths = argv
    else:
        paths = []
        for d in NOTEBOOK_DIRS:
            paths += sorted(glob.glob(os.path.join(ROOT, d, "*.ipynb")))
    total = 0
    for path in paths:
        problems, skipped = check(path, save=save)
        total += len(problems)
        rel = os.path.relpath(path, ROOT)
        status = ("ok" if not problems else f"{len(problems)} problem(s)") + (", saved with outputs" if save else "")
        extra = f", {len(skipped)} cell(s) skipped" if skipped else ""
        print(f"{rel}: {status}{extra}")
        for p in problems:
            print("   ", p)
    print(f"\n{len(paths)} notebook(s) checked, {total} problem(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
