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
