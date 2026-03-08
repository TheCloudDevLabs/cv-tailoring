# Getting Started — Claude Code

This guide walks you through everything you need to install and run the CV tailoring skill using Claude Code (the command-line version of Claude). It assumes no prior experience with the terminal.

---

## What is Claude Code?

Claude Code is Anthropic's version of Claude that runs in a terminal (also called a command prompt or shell). It has access to your local files, which means it can read your CV files, generate Word documents, and save them directly to your computer.

If you'd prefer to work entirely in a browser without any installation, use the [Claude.ai version](getting-started-claude-ai.md) instead.

---

## What you'll need

Before you can use the skill, you need four things installed on your computer:

1. **Node.js** — required to install Claude Code
2. **Claude Code** — the AI that runs the skill
3. **Python** — required to generate Word documents
4. **Git** — required to download the project files

You'll also need an **Anthropic account** to use Claude Code. You can create one at [claude.ai](https://claude.ai).

The sections below walk through installing each one.

---

## Step 1: Install Node.js

Node.js is a programming environment that Claude Code requires to run.

### Windows

1. Go to [nodejs.org](https://nodejs.org/) and click the large **LTS** download button (LTS means "Long Term Support" — the stable version)
2. Run the downloaded installer
3. Accept the defaults on every screen — the installer handles everything
4. When it finishes, open a new Command Prompt or PowerShell window and type:
   ```
   node --version
   ```
   You should see something like `v20.11.0`. If you do, Node.js is installed.

### macOS

If you have Homebrew installed:
```bash
brew install node
```

Otherwise, go to [nodejs.org](https://nodejs.org/) and download the macOS installer, then follow the prompts.

Verify: `node --version`

### Linux (Ubuntu/Debian)

```bash
sudo apt install nodejs npm
```

Verify: `node --version`

---

## Step 2: Install Claude Code

Once Node.js is installed, open a terminal and run:

```bash
npm install -g @anthropic-ai/claude-code
```

This installs Claude Code globally so you can use it from any directory.

To verify it installed correctly:
```bash
claude --version
```

The first time you run `claude`, it will ask you to log in with your Anthropic account. Follow the prompts — it will open a browser window for you to authenticate.

---

## Step 3: Install Python

Python is used to generate the Word document (.docx) at the end of the tailoring process.

### Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click **Download Python**
2. Run the installer
3. **Important:** On the first screen, tick the box that says **"Add Python to PATH"** before clicking Install. This is easy to miss.
4. Verify in a new terminal window:
   ```
   python --version
   ```
   You should see something like `Python 3.11.0`.

If `python` doesn't work, try `python3`.

### macOS

Python 3 is usually pre-installed on modern macOS. Check by opening Terminal and running:
```bash
python3 --version
```

If it's not installed: `brew install python`

### Linux (Ubuntu/Debian)

```bash
sudo apt install python3 python3-pip
```

---

## Step 4: Install Git

Git is used to download the project files.

### Windows

Download and install from [git-scm.com](https://git-scm.com/). Accept the defaults.

Verify: `git --version`

### macOS

Git is usually already installed. If not: `brew install git`

### Linux

```bash
sudo apt install git
```

---

## Step 5: Download the project

Open a terminal in the folder where you want to keep the project (e.g. your Documents folder) and run:

```bash
git clone https://github.com/TheCloudDevLabs/cv-tailoring.git
cd cv-tailoring
```

This creates a `cv-tailoring` folder and puts you inside it.

Then install the Python packages the tool needs:

```bash
pip install python-docx pyyaml
```

(If `pip` doesn't work, try `pip3` or `python -m pip install python-docx pyyaml`)

---

## Step 6: Start Claude Code

From inside the `cv-tailoring` folder, start Claude Code:

```bash
claude
```

You'll see a prompt where you can type commands and chat with Claude. This is where you'll run the skill.

---

## Step 7: Run the setup skill

Type the following and press Enter:

```
/cv-setup
```

The setup skill will guide you through the following steps:

**Personal details** — your name, professional title, email, phone, location, LinkedIn, GitHub (optional), website (optional), and security clearance (if applicable).

**Domain configuration** — which sectors you work in (e.g. government, financial services, technology, healthcare). This determines the writing conventions used in your documents — for example, if you select financial services, the skill uses precise regulatory language; if you select technology, it names specific platforms and services rather than generic "cloud".

**Writing preferences** — spelling convention (Australian, UK, or US English), tone, words you want to avoid, and how to frame collaborative work.

**CV shape** — target page length and which sections to include.

**CV ingestion** — you'll be asked to place your existing CV files into the `cv-variants/` folder before this step. You can have multiple variants (e.g. one focused on architecture, one on security). The setup skill converts any `.docx` files to Markdown for efficient reading in future sessions, and creates an inventory of all variants.

At the end of setup, the skill creates:

- `config.yaml` — your personal configuration
- `references/writing-standards.md` — your personalised writing rules
- `references/cv-variants.md` — an inventory of your CV variants

---

## Step 8: Tailor your first CV

Once setup is complete, you're ready to tailor a CV. In the same Claude Code session (or a new one started from the `cv-tailoring` folder), paste a job description and say something like:

```
Tailor a CV for this:

[paste the job description here]
```

Or if you have a JD as a Word document:

```
Tailor a CV for the JD at cv-tailoring/jds/myjob.docx
```

The skill will:

1. Read all your CV variants
2. Analyse the JD and present a gap analysis
3. Ask you about any gaps in your CV — one gap at a time, with clear options
4. Propose a new profile summary and skills section
5. Work through your employment history role by role
6. Generate a formatted `.docx` CV in the `outputs/` folder
7. Optionally produce a cover letter, selection criteria response, or pitch document

---

## Where files go

All generated files are saved to `outputs/` inside the project folder. Each application gets its own subfolder named with the date, recruiter, organisation, and role:

```
outputs/
└── YYYY-MM-DD_Recruiter_Org_RoleType/
    ├── Your_Name_Role_Type.docx
    └── JD_Org_RoleType.txt
```

The tailored CV is also saved as a Markdown file in `cv-variants/` so it becomes part of your growing library of variants for future sessions.

---

## Updating your setup

If your details change (new contact information, new domain, different preferences), just run `/cv-setup` again from inside Claude Code. You'll be asked which section you want to update — you don't need to redo everything from scratch.

To add new CV variants, place the files in `cv-variants/` and run `/cv-setup` again, selecting the CV ingestion option.

---

## Troubleshooting

**`claude` is not recognised as a command**
Close and reopen your terminal after installing Node.js and Claude Code. If it still doesn't work, try `npx @anthropic-ai/claude-code`.

**`python` is not recognised**
Try `python3` instead. On Windows, if Python was installed without "Add to PATH", re-run the Python installer and tick that option.

**`pip install` fails with a permissions error**
Add `--user` to the end: `pip install --user python-docx pyyaml`

**The skill says it can't find `config.yaml`**
Make sure you started Claude Code from inside the `cv-tailoring` folder (not a parent folder). Run `/cv-setup` to create the config file.

**The generated .docx file looks wrong**
The formatting is handled by `generate_cv.py`. Open an issue on the GitHub repository with a description of what's different from expected.

---

## Next steps

- Read [how it works](how-it-works.md) to understand what's happening behind the scenes
- The `references/writing-standards.md` file can be hand-edited at any time if you want to fine-tune your writing rules — just add notes in the "Custom overrides" section at the bottom
