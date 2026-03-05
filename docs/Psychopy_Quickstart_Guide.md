# Quickstart Guide

**EMA In-Lab Protocol — Tilburg University Lifespan Lab**

> **Who is this guide for?**
> Students with little or no programming experience who need to set up and use
> PsychoPy-based cognitive tasks on a Windows PC. No prior coding knowledge is assumed.

---

## How to Use This Guide

This guide is organized into three levels.

| Level | Goal | Steps to complete |
|-------|------|-------------------|
| **Level 1** | Downloading necessary files |
| **Level 2** | Familiarizing with the new applications | Sections 3 → 4 → 5 → 6 |
| **Level 3** | Edit or adjust an existing task | Sections 1 → 2 → 3 → 4 → 5 → 7 |

---

## The Big Picture: How the Tools Connect

(add image)

| Tool | What it does |
|------|--------------|
| **Miniconda** | Installs and manages Python environments  |
| **psychopy_env** | A Python 3.10 environment pre-loaded with PsychoPy and all required packages to |
| **VS Code** | Code editor where you read, edit, and run experiment scripts |
| **PsychoPy** | The Python library that actually runs cognitive tasks |
| **Pavlovia** | Hosts the web version of tasks so participants can do them on a phone |
| **m-Path** | Sends scheduled notifications to participants and links them to Pavlovia |

---

## Section 1 — Enable Script Execution (Windows only)

Windows blocks scripts by default. You must change this setting once before anything else will work. This is the first line of code you going to run!

1. Press `Win`, type **PowerShell**, right-click it, and choose **Run as administrator**.
2. Paste the following command and press `Enter`:
   
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Type `Y` and press `Enter` if prompted to confirm.
4. Close PowerShell.

> **Why?** Without this change, Conda and many other tools will silently fail to activate environments or run scripts on Windows.

---

## Section 2 — Downloads Checklist

Complete these downloads before starting any other step.

### 2a. Required for all levels

| # | What | Where to get it | Notes |
|---|------|-----------------|-------|
| 1 | **VS Code** | [Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/Download) | Choose the Windows installer or MacOs depending on your PC |
| 2 | **Miniconda** | [Download Anaconda Distribution Anaconda](https://www.anaconda.com/download) | Scroll to the bottom to find miniconda installer and follow the installation process |
| 3 | **psychopy_env.yml** | [github.com/rcarrioncanonico/Momentary-Assesment-Tools](https://github.com/rcarrioncanonico/Momentary-Assesment-Tools/blob/main/psychopy_env.yml) | Click **Raw**, then `Ctrl+S` to save as `psychopy_env.yml` |
| 4 | **Git** | [Git - Install](https://git-scm.com/install/) | Necessary to Push code to Pavlovia |

### 2b. Needed Accounts

| # | What | Where to get it | Notes |
|---|------|-----------------|-------|
| 5 | **Github** | [GitHub](https://github.com/) | Needed to sync with VS-Code and to access AI Copilot for easy coding |
| 6 | **Pavlovia account** | [pavlovia.org](https://pavlovia.org/) | Free for researchers |
| 7 | **m-Path account** | [m-path.io](https://m-path.io/) | Coordinate with your supervisor |

### 2c. Optional ( To see if the Psychopy Enviroment was Installed Correctly)

| # | What | Where to get it | Notes |
|---|------|-----------------|-------|
| 8 | **PsychoPy Standalone** | [psychopy.org/download.html](https://www.psychopy.org/download.html) | Recommended |

---

## Section 3 — Miniconda Use

---

Once Miniconda is intalled you will have a new application called **Anaconda Prompt** which looks like this:

(image)

To build the `psychopy_env` workspace that we need for all scripts to run PsychoPy tasks we need to:

1. Press `Win`, type **Anaconda Prompt**, and open it.
2. Change to the folder where you saved `psychopy_env.yml`. You can do this by copying and pasting the code below. For example, if you saved it in Downloads:

```cmd
cd %USERPROFILE%\Downloads
          or if you have psychopy_env.yml saved in Documents
cd %USERPROFILE\Documents
```

3. Create the PsychoPy environment by running this code:
   
   ```cmd
   conda env create -f psychopy_env.yml
   ```
   
   This downloads and installs all required packages. It may take 5–15 minutes.
4. Confirm it succeeded — you should see a `psychopy_env` folder here:
   
   ```
   C:\Users\<YourName>\miniconda3\envs\psychopy_env\
   ```
   
   You can also check by running this code in **Anaconda Prompt**:
   
   ```cmd
   conda env list
   ```
   
   `psychopy_env` should appear in the list.

---

## Section 4 — VS Code Familirization

### 4a. User Interface

VS-Code can be a little bit confusing and overwhelming as soon as you start it up, don´t worry the user-interface is pretty friendly once you get use to it.

Since It is better to see someone use VS-Code rather than in text I recommend you to watch the first 7 minutes of this video which explains the "Explorer" part of the "Activity Bar"

[VS Code for Absolute Beginners](https://www.youtube.com/watch?v=lWEKiak0WVU)

Also I recommend to watch the first 12 minutes of this video which gets more in depth of the different activity bar uses and AI chat functions

[Learn Visual Studio Code in 15 minutes: 2026 Official Beginner Tutorial - YouTube](https://www.youtube.com/watch?v=f8_uF_IDV50)

### 4a. Installing Necessary Extension

As this tutorial is based on using VS-Code we are going to need to install some extensions 

1. Open VS Code.
2. Click the **Extensions** icon in the left sidebar (it looks like four squares, or press `Ctrl+Shift+X`).
3. Search for **Python** (publisher: Microsoft) and click **Install**.

### 4b. Open the project folder

1. In VS Code, go to **File → Open Folder**.
2. Select the folder that contains the experiment files (e.g. `nBackAlpha3-master`).
   
   > **Important:** Always open the experiment's own folder, not a parent folder. This ensures all file paths in the scripts point to the right places.

### 4c. Select the Python interpreter

1. Look at the **bottom-right corner** of the VS Code window. You will see a Python version number (e.g. `Python 3.11.x`).
   
   ```
   ┌─────────────────────── VS Code status bar ───────────────────────┐
   │                                            [Python 3.11.x] [⚡]  │
   └──────────────────────────────────────────────────────────────────┘
                                                        ▲
                                               click here
   ```
2. Click that version number. A list appears at the top of the screen.
3. Choose the entry that contains **psychopy_env** — it will look something like:
   
   ```
   Python 3.10.x ('psychopy_env': conda)
   ```

### 4d. Activate the environment in the terminal

1. Go to **Terminal → New Terminal** (or press ``Ctrl+` ``).
2. The terminal should automatically show `(psychopy_env)` at the start of the prompt:
   ```
   (psychopy_env) PS C:\Users\YourName\...>
   ```
3. If it does not activate automatically, type:
   ```cmd
   conda activate psychopy_env
   ```

---

## Section 5 — Run a Task (Level 1+)

### Verify PsychoPy works first

Before running a real experiment, confirm your setup is correct:

1. In VS Code, open a new file (`Ctrl+N`), paste the code below, and save it as `sanity_check.py` inside your project folder.
   
   ```python
   from psychopy import visual
   import time
   
   win = visual.Window([800, 600], color='black', monitor='testMonitor')
   text = visual.TextStim(win, text='PsychoPy is Working!', color='white', height=0.1)
   text.draw()
   win.flip()
   time.sleep(2)
   win.close()
   print('Sanity check complete!')
   ```
2. Right-click the file in the Explorer panel on the left → **Run Python File in Terminal**.
3. A black window should appear for 2 seconds with the text **"PsychoPy is Working!"**, then close.
4. The terminal should print `Sanity check complete!`

> If you see an error instead, see the Troubleshooting section at the end of this guide.

### Run the N-back task

1. In VS Code Explorer, navigate to `nBackAlpha3-master`.
2. Right-click `nBackAlpha3.py` → **Run Python File in Terminal**.
3. The task window will appear. Press `s` to start the trials.

---

## Section 6 — EMA Deployment Pipeline (Level 2)

To deliver tasks to participants via their smartphones:

```
Your .py task  →  push to Pavlovia  →  Pavlovia hosts web version
                                                 ↑
                                         m-Path sends notification link
                                         to participant's phone
```

1. **Push to Pavlovia**: Commit your task folder to a Pavlovia-linked GitLab repository. Your supervisor will help you set this up.
2. **Set task to Running**: In the Pavlovia dashboard, change the experiment status from *Piloting* to *Running*.
3. **Configure m-Path**: In the m-Path study configuration, paste the Pavlovia task URL. m-Path will embed it in participant notifications.
4. **Test end-to-end**: Have a test participant (yourself) receive a notification and complete the task on a phone to verify the full pipeline.

---

## Section 7 — Editing a Task (Level 3)

Before making any changes:

1. **Make a backup**: Copy the entire experiment folder and rename the copy (e.g. append `_backup_YYYYMMDD`).
2. Open the `Configuration_Modification_Tutorial.ipynb` notebook in VS Code for step-by-step guidance on which parameters to change.
3. Common edit targets in `nBackAlpha3.py`:
   
   | What you want to change | Variable to edit |
|-------------------------|-----------------|
| How long each stimulus appears | `trialClock` duration / `time.sleep()` value |
| Number of trials | `nReps` in the trial loop |
| Stimulus size or color | `height`, `color` arguments in `TextStim` or `ImageStim` |
   
   
4. After each change, re-run the sanity check (Section 5) and then run the task briefly to verify nothing broke.

---

## Terminal Quick Reference

| Situation | What to type |
|-----------|-------------|
| Activate environment | `conda activate psychopy_env` |
| Check active environment | `conda info --envs` |
| You see `>>>` (Python REPL) | Type `exit()` to return to normal terminal |
| Run a Python file | `python filename.py` |
| Re-create environment from scratch | `conda env create -f psychopy_env.yml` |
| List installed packages | `conda list` |

### Understanding the two terminal modes

```
Normal terminal (PowerShell):        Python REPL (interactive Python):
  (psychopy_env) PS C:\> _               >>>  _
        ▲                                      ▲
  Run: python script.py             Stuck here? Type: exit()
       conda commands
```

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `conda: command not found` | Miniconda not added to PATH | Reinstall Miniconda and check "Add to PATH" option |
| `psychopy_env.yml not found` | Wrong directory in Anaconda Prompt | Run `cd %USERPROFILE%\Downloads` (or wherever you saved the file) |
| VS Code shows wrong Python version | Interpreter not set | See Section 4c |
| PsychoPy window opens then instantly crashes | `core.quit()` called in Jupyter context | Remove `core.quit()` calls; use `win.close()` only |
| `FileNotFoundError` when running task | Wrong working directory | Ensure you opened the experiment folder in VS Code (Section 4b) |
| Scripts won't run in terminal | Windows execution policy | Re-run the command in Section 1 as administrator |
| `ModuleNotFoundError: psychopy` | Wrong environment active | Activate `psychopy_env` (Section 4d) |

---

## Further Reading

| Resource | URL | Best for |
|----------|-----|---------|
| Neural Data Science setup guide | https://neuraldatascience.io/b-setup/introduction/ | Complete beginner setup |
| Pro Git Book | https://git-scm.com/book/en/v2 | Learning Git version control |
| Pavlovia documentation | https://pavlovia.org/docs | Deploying experiments online |
| m-Path manual | https://manual.m-path.io/ | EMA scheduling and linking |
| PsychoPy documentation | https://www.psychopy.org/documentation.html | Experiment scripting reference |

---

*Tilburg University Lifespan Lab — EMA In-Lab Protocol*
*For questions, contact your supervisor or open an issue on the project GitHub repository.*