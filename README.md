# MA Digital Text Analysis: Bootcamp (2026-2027)

The bootcamp is the first, intensive module of the [MA Digital Text Analysis](https://www.uantwerpen.be/en/study/programmes/all-programmes/digital-text-analysis/) at the University of Antwerp. In three weeks it takes you from zero programming experience to the core of Python that every later module builds on: variables, data types, control structures, files, functions, strings, regular expressions, comprehensions, `pandas` and objects. Think of it as a language immersion course: we do not cover everything Python can do, only what you will actually use in this programme, and we practise it a lot.

- **Dates:** Monday 21 September to Friday 9 October 2026
- **First point of contact:** [Jens Lemmens](mailto:jens.lemmens@uantwerpen.be)
- **Material:** this repository. Every session is a Jupyter notebook in `notebooks/`, with an exercise notebook in `exercises/questions/` and worked solutions in `exercises/solutions/`.

Contents of this page:

1. [Timetable](#1-timetable)
2. [Before the bootcamp: install Python and get the material](#2-before-the-bootcamp-install-python-and-get-the-material)
3. [What is a notebook and how do I use it?](#3-what-is-a-notebook-and-how-do-i-use-it)
4. [Google Colab (and its limits)](#4-google-colab-and-its-limits)
5. [Exercises and solutions](#5-exercises-and-solutions)
6. [When something goes wrong](#6-when-something-goes-wrong)
7. [Tutors, licence, credits](#7-tutors-licence-credits)

## 1. Timetable

Morning sessions run from 10:30 to 12:30, afternoon sessions from 14:00 to 16:00. Every session has a tutor and an assistant who walks around and helps. Sessions marked *Troubleshooting* are optional: come by with your own questions, or finish the exercises of the morning.

For each notebook there are three links: **view** it on GitHub, **download** the `.ipynb` file to run it on your own computer, or **open** it in Google Colab (see [section 4](#4-google-colab-and-its-limits)). Notebooks are sometimes updated the evening before a session, so download the notebook you need at the start of each session.

Notebook names follow one pattern, for example `06_W2_Mon_Input_Output_Files.ipynb`: a two-digit number that fixes the order of the sessions (`06`), the week (`W2`) and weekday (`Mon`) on which the session is taught, and the topic. The matching exercise notebook has the same number with the prefix `EX` (`06_EX_Input_Output_Files.ipynb`), its solutions the prefix `SOL` (`06_SOL_Input_Output_Files.ipynb`).

### Week 1

| Day | Time | Room | Session | Tutor / assistant |
| --- | --- | --- | --- | --- |
| Mon 21/09 | | | City walk | |
| Tue 22/09 | 10:30 | S.D.328 | Course overview and getting started: `01` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/01_W1_Tue_Ma_DTA_Course_Overview.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/01_W1_Tue_Ma_DTA_Course_Overview.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/01_W1_Tue_Ma_DTA_Course_Overview.ipynb) | Jens Lemmens, Luna De Bruyne, Mike Kestemont |
| Tue 22/09 | 14:00 | S.D.328 | Python and variables: `02` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/02_W1_Tue_Python_and_Variables.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/02_W1_Tue_Python_and_Variables.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/02_W1_Tue_Python_and_Variables.ipynb) | Luna De Bruyne / Jens Van Nooten |
| Wed 23/09 | 10:30 | S.R.213 | Data types, lists, dictionaries: `03` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/03_W1_Wed_Data_Types_Lists_Dictionaries.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/03_W1_Wed_Data_Types_Lists_Dictionaries.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/03_W1_Wed_Data_Types_Lists_Dictionaries.ipynb) | Luna De Bruyne / TBD |
| Wed 23/09 | 14:00 | S.R.213 | Control structures: if and else: `04` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/04_W1_Wed_Control_structures_if_else.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/04_W1_Wed_Control_structures_if_else.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/04_W1_Wed_Control_structures_if_else.ipynb) | Mike Kestemont / Caroline Vandyck |
| Thu 24/09 | | | No classes (StuDay) | |
| Fri 25/09 | 10:30 | S.SJ.214 | Control structures: loops: `05` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/05_W1_Fri_Control_Structures_Loops_For_While.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/05_W1_Fri_Control_Structures_Loops_For_While.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/05_W1_Fri_Control_Structures_Loops_For_While.ipynb) | Jens Lemmens / TBD |
| Fri 25/09 | 14:00 | S.D.226 | Exercises: variables, data types (`02_EX`, `03_EX`) | Mike Kestemont / TBD |

### Week 2

| Day | Time | Room | Session | Tutor / assistant |
| --- | --- | --- | --- | --- |
| Mon 28/09 | 10:30 | S.SJ.117 | Input, output and files: `06` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/06_W2_Mon_Input_Output_Files.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/06_W2_Mon_Input_Output_Files.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/06_W2_Mon_Input_Output_Files.ipynb) | Mike Kestemont / TBD |
| Mon 28/09 | 14:00 | S.SJ.117 | Frequency distributions: `07` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/07_W2_Mon_Frequency_Distribution_in_Python_Counting_Text.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/07_W2_Mon_Frequency_Distribution_in_Python_Counting_Text.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/07_W2_Mon_Frequency_Distribution_in_Python_Counting_Text.ipynb) | Luna De Bruyne / TBD |
| Tue 29/09 | 10:30 | S.D.328 | Exercises: if-else, loops, files, frequencies (`04_EX` to `07_EX`) | TBD / TBD |
| Tue 29/09 | 14:00 | S.D.328 | Troubleshooting (optional) | Jens Van Nooten |
| Wed 30/09 | 10:30 | S.R.213 | Functions: `08` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/08_W2_Wed_Functions.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/08_W2_Wed_Functions.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/08_W2_Wed_Functions.ipynb) | Jens Lemmens / TBD |
| Wed 30/09 | 14:00 | S.R.213 | String manipulation: `09` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/09_W2_Wed_String_Manipulation.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/09_W2_Wed_String_Manipulation.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/09_W2_Wed_String_Manipulation.ipynb) | TBD / Caroline Vandyck |
| Thu 01/10 | 10:30 | S.D.328 | Exercises: functions, strings (`08_EX`, `09_EX`) | Jens Van Nooten / TBD |
| Thu 01/10 | 14:00 | S.D.328 | Troubleshooting (optional) | Jens Lemmens |
| Fri 02/10 | 10:30 | S.D.226 | Regular expressions: `10` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/10_W2_Fri_Regular_Expressions.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/10_W2_Fri_Regular_Expressions.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/10_W2_Fri_Regular_Expressions.ipynb) | Febe Thonissen / TBD |
| Fri 02/10 | 14:00 | S.D.226 | Functional programming and comprehensions: `11` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/11_W2_Fri_Functional_Programming_List_Comprehensions.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/11_W2_Fri_Functional_Programming_List_Comprehensions.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/11_W2_Fri_Functional_Programming_List_Comprehensions.ipynb) | Luna De Bruyne / Mike Kestemont |

### Week 3

| Day | Time | Room | Session | Tutor / assistant |
| --- | --- | --- | --- | --- |
| Mon 05/10 | 10:30 | S.SJ.117 | The command line (slides) | Jens Van Nooten / TBD |
| Mon 05/10 | 14:00 | S.SJ.117 | Project work: `12` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/12_W3_Mon_Larger_Project.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/12_W3_Mon_Larger_Project.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/12_W3_Mon_Larger_Project.ipynb) | Jens Lemmens / TBD |
| Tue 06/10 | 10:30 | S.D.328 | Exercises: regular expressions, functional programming (`10_EX`, `11_EX`) | Mike Kestemont / TBD |
| Tue 06/10 | 14:00 | S.D.328 | Troubleshooting (optional) | Febe Thonissen |
| Wed 07/10 | 10:30 | S.R.118 | `pandas`: `13` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/13_W3_Wed_Pandas.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/13_W3_Wed_Pandas.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/13_W3_Wed_Pandas.ipynb) | Loren Verreyen / Caroline Vandyck |
| Wed 07/10 | 14:00 | S.C.102 | Object orientation: `14` [view](https://github.com/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/14_W3_Wed_Object_Orientation.ipynb) / [download](https://raw.githubusercontent.com/mikekestemont/dtaantwerp26-27.github.io/DTA_Bootcamp_2026_students/notebooks/14_W3_Wed_Object_Orientation.ipynb) / [colab](https://colab.research.google.com/github/mikekestemont/dtaantwerp26-27.github.io/blob/DTA_Bootcamp_2026_students/notebooks/14_W3_Wed_Object_Orientation.ipynb) | Victor De Marez / TBD |
| Thu 08/10 | 10:30 | S.D.328 | Exercises: `pandas` (`13_EX`) | Loren Verreyen / Caroline Vandyck |
| Thu 08/10 | 14:00 | S.D.328 | Working with large language models: `15` (notebook to follow) | Pieter Fivez (tentative) |
| Fri 09/10 | 10:30 | S.D.226 | Information session: thesis, internship, practicum | Jens Lemmens and the thesis supervisors |
| Fri 09/10 | 14:00 | S.D.226 | Troubleshooting (optional) | Jens Lemmens |

Exercise notebooks: [`exercises/questions/`](https://github.com/mikekestemont/dtaantwerp26-27.github.io/tree/DTA_Bootcamp_2026_students/exercises/questions). Solutions: [`exercises/solutions/`](https://github.com/mikekestemont/dtaantwerp26-27.github.io/tree/DTA_Bootcamp_2026_students/exercises/solutions). Data files used by the notebooks: [`data/`](https://github.com/mikekestemont/dtaantwerp26-27.github.io/tree/DTA_Bootcamp_2026_students/data).

## 2. Before the bootcamp: install Python and get the material

Please do this **before Tuesday 22 September**. It takes about half an hour, most of which is waiting for a download. If anything fails, that is fine: bring your laptop to the first session and we will sort it out together.

### 2.1 Install Anaconda

We use the **Anaconda Distribution**: one installer that gives you Python, Jupyter and all the libraries we need (`pandas`, `matplotlib`, ...). It works the same way on Windows, macOS and Linux and does not interfere with anything else on your computer.

1. Go to [anaconda.com/download](https://www.anaconda.com/download). You can skip the registration form ("Skip registration" or a similar link under the form).
2. Download the **graphical installer** for your operating system:
   - **Windows:** the 64-bit installer.
   - **macOS:** there are two installers. Click the Apple menu, choose *About This Mac* and look at *Chip* (or *Processor*): if it says *Apple M1/M2/M3/M4...* take the **Apple Silicon** installer, if it says *Intel* take the **Intel** installer.
   - **Linux:** the `.sh` installer; run it in a terminal with `bash Anaconda3-*.sh` and accept the defaults.
3. Run the installer and accept the defaults ("Just Me", default location). You need about 5 GB of free disk space. On Windows, **tick** the box "Add Anaconda to my PATH environment variable" when it appears (the installer advises against it, but it makes `python` and `jupyter` available from the command prompt, which you will need in the command-line session of week 3).
4. When the installer is done, start **Anaconda Navigator** (Windows: Start menu; macOS: Applications folder or Launchpad). The first start is slow; that is normal.

Any recent Anaconda version will do; the notebooks work with Python 3.10 or newer.

### 2.2 Get the course material

The material lives in this repository (a GitHub repository is simply a folder that is shared online).

1. On the [repository page](https://github.com/mikekestemont/dtaantwerp26-27.github.io/tree/DTA_Bootcamp_2026_students), click the green **Code** button and choose **Download ZIP**.
2. Unzip the file and move the resulting folder to a place where you will find it again, for instance `Documents/bootcamp`.
3. Do **not** rename or move the folders inside it. The notebooks in `notebooks/` expect the data files to be in the neighbouring `data/` folder.

The notebooks are updated during the bootcamp. At the start of each session, download the notebook of that session from the timetable above (the **download** link) and save it into your `notebooks/` folder, replacing the old copy. Some browsers show the file as text instead of downloading it; in that case right-click the link and choose *Save link as...*, and make sure the file name ends in `.ipynb`.

### 2.3 Start Jupyter and open a notebook

1. In Anaconda Navigator, click **Launch** under **Jupyter Notebook**. A tab opens in your web browser showing the files in your home folder. (JupyterLab, also listed in Navigator, is a more elaborate interface for the same thing; you can use either.)
2. Navigate to your `bootcamp/notebooks/` folder and click a notebook to open it.
3. Jupyter keeps running in a black terminal window or in the Navigator in the background. Do not close that window while you work.

To check that everything works, open `01_W1_Tue_Ma_DTA_Course_Overview.ipynb`, click on the first code cell and press **Shift+Enter**. If `Hello, world!` appears below the cell, you are ready.

### 2.4 A note on other editors (VS Code)

Notebooks can also be opened in [Visual Studio Code](https://code.visualstudio.com/), a free editor that you will use in later courses of the programme and that many of us use daily. It is a very nice environment, but it comes with built-in code completion and AI assistance, which you will **not** be able to use at the exam. For the bootcamp we therefore prefer the plain Jupyter Notebook interface: it is the environment of the exam, and learning to write code without a machine finishing your sentences is exactly the point of these three weeks.

## 3. What is a notebook and how do I use it?

A **Jupyter notebook** is a document (a file ending in `.ipynb`) that mixes text and runnable code. It is the standard working environment for data analysis, and it is what we use in every session of this programme.

A notebook consists of **cells**. There are two kinds:

- **Markdown cells** contain text (explanations, headings, links). Double-click a text cell to see its source; run it to render it again.
- **Code cells** contain Python. When you run a code cell, Python executes it and shows the result underneath. The `In [3]:` label on the left tells you that this was the third cell you ran.

Things you will do all the time:

- **Run a cell:** click in it and press **Shift+Enter** (runs the cell and moves to the next one). **Ctrl+Enter** runs it and stays put.
- **Add a cell:** the `+` button in the toolbar, or press **Esc** and then **B** (below) or **A** (above).
- **Change the cell type:** the dropdown in the toolbar (Code / Markdown), or **Esc** then **M** or **Y**.
- **Delete a cell:** **Esc** then **D**, **D**.
- **Save:** **Ctrl+S** (Windows, Linux) or **Cmd+S** (macOS). Jupyter also saves every few minutes.

Behind the notebook runs a Python process called the **kernel**. It remembers every variable you define, in the order in which you ran the cells, not in the order in which they appear on the page. Two consequences:

- If a cell says `NameError: name 'text' is not defined`, you probably skipped the cell that defines `text`. Run that one first.
- To make sure your notebook works from top to bottom (which is what we ask at the exam), use the menu **Kernel > Restart Kernel and Run All Cells**. This forgets everything and re-runs the whole notebook in order.

If a cell runs forever (an infinite loop, or `input()` waiting for you), press the **stop** button or choose **Kernel > Interrupt**.

## 4. Google Colab (and its limits)

Every notebook in the timetable has a **colab** link that opens it in [Google Colab](https://colab.research.google.com), a free service that runs notebooks on Google's computers in your browser. It is useful as a **back-up**: when your laptop is not set up yet, when a library refuses to install, or when you want to look at a notebook on a tablet. It is not the way we expect you to work, for the following reasons.

- Colab needs a Google account.
- Colab does not see the files on your computer or the `data/` folder of this repository. Notebooks that read files therefore start with a cell marked *"Run this cell only on Google Colab"*, which downloads the material. Run it first; it does no harm on your own computer either.
- Your changes are **not** saved automatically. To keep your work, use *File > Save a copy in Drive* or *File > Download > Download .ipynb*. If you just close the tab, your work is gone.
- A Colab session stops after a period of inactivity and all variables are lost; you then have to re-run the notebook.
- **At the exam you work on your own computer, in Jupyter, without Colab.** Practise that way from the start.

## 5. Exercises and solutions

Each session notebook has a matching exercise notebook in `exercises/questions/` (same number, prefix `EX`). Every exercise notebook has two parts:

- **Core exercises:** prepare these **before** the practice session of that week. They cover the essentials and should take one to two hours if you followed the class.
- **Extra exercises:** more challenging, or for practising further. Good material for the troubleshooting sessions.

Worked solutions are in `exercises/solutions/` (same number, prefix `SOL`). Look at them after you have tried an exercise yourself, and remember that there is usually more than one correct solution.

## 6. When something goes wrong

Errors are a normal part of programming; the notebooks will teach you how to read them. A few classics:

| You see | What it usually means | What to do |
| --- | --- | --- |
| `FileNotFoundError: [Errno 2] No such file or directory: '../data/alice.txt'` | Python is looking for the file relative to the folder the notebook is in, and does not find it there. | Check that your notebook is inside `notebooks/` and the data inside the neighbouring `data/` folder. Run `import os; print(os.getcwd())` to see where the notebook is running. On Colab, run the "Colab only" cell first. |
| `UnicodeDecodeError` when opening a text file | Your operating system uses a different default character encoding than the file (this mostly happens on Windows). | Always open text files with `open(path, encoding='utf-8')`. The notebooks do this consistently. |
| `NameError: name '...' is not defined` | You ran cells out of order, or restarted the kernel and did not re-run earlier cells. | Run the earlier cells, or *Kernel > Restart Kernel and Run All Cells*. |
| `ModuleNotFoundError: No module named '...'` | A library is not installed. Everything we use comes with Anaconda, so this normally means Jupyter was started outside Anaconda. | Start Jupyter from Anaconda Navigator. If a package is really missing, install it from Navigator's *Environments* tab. |
| The cell shows `[*]` and nothing happens | The cell is still running: an infinite loop, or an `input()` box waiting for you (look for a text box under the cell). | Type an answer, or *Kernel > Interrupt*. |
| The downloaded notebook opens as a wall of text | The browser saved the file as text, or you opened it in a text editor. | Make sure the file ends in `.ipynb` and open it through Jupyter, not by double-clicking. |

If you are stuck, ask the assistant during the session, come to a troubleshooting session, or email [Jens Lemmens](mailto:jens.lemmens@uantwerpen.be).

## 7. Tutors, licence, credits

**Tutors 2026-2027:** Luna De Bruyne, Victor De Marez, Pieter Fivez, Mike Kestemont, Jens Lemmens, Febe Thonissen, Jens Van Nooten, Caroline Vandyck, Loren Verreyen. All of us can be reached at `firstname.lastname@uantwerpen.be`.

**Licence:** this material is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): you may share and adapt it for non-commercial purposes, with attribution. The texts in `data/` come from [Project Gutenberg](https://www.gutenberg.org/) and are in the public domain; the other data files are described in `data/README.md`.

**Credits:** the notebooks have been developed and revised by the tutors of the MA Digital Text Analysis over many years. Their solutions, mistakes and jokes are theirs; the typos are ours.
