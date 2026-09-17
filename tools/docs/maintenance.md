# Maintenance scripts (for tutors)

These scripts are for the tutors, not for the students. Run them from the
repository root with the Python that comes with Anaconda (they need
`nbformat`, `nbclient` and `ipykernel`, which Anaconda installs).

| Script | What it does |
| --- | --- |
| `config.py` | Owner, repository and branch used in all generated links. Edit this when the material moves to another repository. |
| `build_headers.py` | Rewrites the header cell of every notebook (title, Colab badge, and a "Colab only" data cell where the notebook reads files) from the notebook's own title. Run after adding or renaming a notebook. |
| `check_notebooks.py` | Executes every notebook from top to bottom in a fresh kernel and reports every cell that fails or warns, except cells tagged `raises-on-purpose`, `needs-input` or `skip-check`. Files written by the notebooks are removed afterwards. Run before every push. |
| `check_links.py` | Collects every URL in the notebooks and Markdown files and reports the ones that do not answer with HTTP 200. |

Typical use:

```bash
python tools/build_headers.py
python tools/check_notebooks.py            # all notebooks
python tools/check_notebooks.py notebooks/06_W2_Mon_Input_Output_Files.ipynb
python tools/check_notebooks.py --save exercises/solutions/06_SOL_Input_Output_Files.ipynb   # solutions: keep outputs
python tools/check_links.py
```

## Cell tags

Some cells are supposed to fail (a demonstration of a `TypeError`), and some
need a person at the keyboard (`input()`). Mark those with a cell tag so that
the checker knows: in Jupyter Notebook choose *View > Cell Toolbar > Tags*
(or open the property inspector in JupyterLab) and add one of

- `raises-on-purpose`: the cell must raise an exception; the checker reports it if it does *not*;
- `needs-input`: the cell calls `input()`; the checker skips it;
- `skip-check`: skip for any other reason (long downloads, deliberately unfinished code in an exercise).

By convention such cells also start with a comment for the students, e.g.
`# This cell produces an error on purpose:`.

## Writing conventions for the notebooks

- Plain Markdown, no HTML boxes; headings `##` for sections, `###` for subsections (the `#` title lives in the generated header).
- Do not refer to other sessions by weekday, time or week ("this afternoon", "on Friday", "next week"): the schedule changes from year to year. Refer to sessions by topic ("the session on loops", "the next session"). `check_notebooks.py` flags such phrases.
- No dates, tutor names or repository links in the body of a notebook; the header cell carries those and is generated from the README.
- British spelling; second person; no emoji.
- f-strings for formatting; `encoding='utf-8'` in every `open()`; raw strings for every regular expression; `with open(...)` once it has been introduced.
- Cells that are meant to fail start with `# This cell produces an error on purpose` and carry the tag `raises-on-purpose`; cells that call `input()` carry `needs-input`.
- Teaching and exercise notebooks are committed without outputs; solution notebooks with outputs (`python tools/check_notebooks.py --save exercises/solutions/NN_SOL_*.ipynb`).
- Class exercises in a session notebook get an empty `# your code here` cell (tagged `skip-check`) and **no solution cell**: they are solved together in class. Their solutions go at the end of the matching solutions notebook, under *Class exercises from the session notebook*.
- Exercise notebooks: a *Core exercises* section (about 8, to prepare before the practice session) and an *Extra exercises* section (about 6-8), numbered consecutively, each with a title and a level (basic / standard / harder).
- Exercises may introduce a small new function or method that the session did not cover, **with guidance**: the exercise text explains it and shows an example before asking for it. This keeps the sessions short without hiding useful things. Examples: `input()` with casting (`03_EX` no. 9), `round()` (an exercise on printing numbers), `enumerate()` (an exercise in the strings set), `.join()` as the inverse of `.split()`. Anything a *later session* depends on must still be taught in a session, not only in an exercise.
