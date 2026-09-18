"""Settings shared by the scripts in tools/.

Change OWNER/REPO/BRANCH here when the material moves to another repository
(for instance from a tutor's fork to the students' repository): the notebook
headers are rebuilt from these values by build_headers.py. The links in
README.md are hand-written; update them with a search-and-replace.
"""

OWNER = "LemmensJens"
REPO = "dtaantwerp26-27.github.io"
BRANCH = "DTA_Bootcamp_2026_students"

GITHUB_URL = f"https://github.com/{OWNER}/{REPO}"
BLOB_URL = f"{GITHUB_URL}/blob/{BRANCH}"
RAW_URL = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}"
COLAB_URL = f"https://colab.research.google.com/github/{OWNER}/{REPO}/blob/{BRANCH}"

# Folders that contain notebooks, relative to the repository root.
NOTEBOOK_DIRS = ["notebooks", "exercises/questions", "exercises/solutions"]

# Cell tags (Jupyter: View > Cell Toolbar > Tags) understood by check_notebooks.py
TAG_RAISES = "raises-on-purpose"   # the cell demonstrates an error; an exception is expected
TAG_INPUT = "needs-input"          # the cell calls input(); skipped when run without a keyboard
TAG_SKIP = "skip-check"            # anything else that should not be executed by the checker

# Academic year of the session dates in the README timetable.
YEAR = 2026
