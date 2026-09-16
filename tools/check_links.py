"""Report every URL in the notebooks and Markdown files that does not answer with HTTP 200.

Usage (from the repository root):

    python tools/check_links.py

Links to this repository itself are checked too, so the script also catches
timetable entries that point to a notebook that was renamed.
"""

import os
import re
import sys
import glob
import json
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import NOTEBOOK_DIRS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = re.compile(r"https?://[^\s<>()\"'`\]\[]+")
HEADERS = {"User-Agent": "Mozilla/5.0 (link checker for the DTA bootcamp material)"}


def urls_in(text):
    return {u.rstrip(".,;:") for u in URL.findall(text)}


def collect():
    found = {}
    files = glob.glob(os.path.join(ROOT, "*.md")) + glob.glob(os.path.join(ROOT, "*", "*.md"))
    for d in NOTEBOOK_DIRS:
        files += glob.glob(os.path.join(ROOT, d, "*.ipynb"))
    for path in files:
        rel = os.path.relpath(path, ROOT)
        if path.endswith(".ipynb"):
            nb = json.load(open(path, encoding="utf-8"))
            text = "\n".join("".join(c["source"]) for c in nb["cells"])
        else:
            text = open(path, encoding="utf-8").read()
        for u in urls_in(text):
            found.setdefault(u, set()).add(rel)
    return found


def status(url):
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return type(e).__name__


def main():
    found = collect()
    bad = 0
    for url in sorted(found):
        code = status(url)
        if code != 200:
            bad += 1
            print(f"{code}\t{url}\n\tin: {', '.join(sorted(found[url]))}")
    print(f"\n{len(found)} link(s) checked, {bad} problem(s).")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
