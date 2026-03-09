# CV Tailoring — AI-Powered CV Customisation

A skill for Claude that tailors your CV to specific job descriptions through conversation. Paste a job description, answer a few questions about your experience, and get a professionally formatted CV tailored to that role — along with cover letters, selection criteria responses, and pitch documents if needed.

---

## Which option is right for me?

There are two ways to use this tool. Both do the same job — choose based on what you're comfortable with.

| | Claude Code | Claude.ai |
|---|---|---|
| **What it is** | Claude in your terminal | Claude in your browser |
| **Technical setup** | Requires installing a few tools | No installation — browser only |
| **Best for** | Developers, technical users | Anyone |
| **Output files** | Saved directly to your computer | Downloaded from Claude |
| **Setup guide** | [Getting started — Claude Code](docs/getting-started-claude-code.md) | [Getting started — Claude.ai](docs/getting-started-claude-ai.md) |

If you've never used a terminal before, **start with Claude.ai**. If you're comfortable with the command line, either option works well.

---

## What it does

Once set up, the skill walks you through tailoring your CV to a specific job description:

1. **Reads all your CV variants** — you can have multiple versions emphasising different things (e.g. one focused on architecture, one on security)
2. **Analyses the job description** — identifies what the role requires and where your existing CV needs to be repositioned or expanded
3. **Asks targeted questions** — works through any gaps one at a time using structured prompts, so you're never asked to write from scratch
4. **Proposes changes** — suggests a new profile summary and skills section, then works through your employment history role by role
5. **Generates a formatted CV** — produces a clean, professionally formatted `.docx` file ready to submit
6. **Produces supporting documents** — optionally generates cover letters, selection criteria responses, and pitch documents

Everything is written in your voice, using your actual experience, following the writing preferences you configure during setup.

---

## How setup works

Before using the tailoring skill, you run a one-time setup that:

- Collects your personal details (name, contact, LinkedIn, clearance, etc.)
- Asks about your industry domains so writing standards are appropriate for your field
- Configures your writing preferences (spelling, tone, words to avoid)
- Ingests your existing CV files and creates an inventory of them
- Generates a `config.yaml` and a personalised `writing-standards.md` — the two files the tailoring skill reads before doing anything

If your details change or you want to update your preferences, you can re-run setup at any time.

---

## Quick start

### Claude Code

```bash
git clone https://github.com/TheCloudDevLabs/cv-tailoring.git
cd cv-tailoring
pip install python-docx pyyaml
claude
```

Then in Claude Code, type `/cv-setup` and follow the prompts.

Full guide: [docs/getting-started-claude-code.md](docs/getting-started-claude-code.md)

### Claude.ai

1. Build the setup skill file from this repository:

   **macOS / Linux:**
   ```bash
   cd cv-tailoring
   (cd .claude.ai/skills && zip -r ../../cv-tailoring-setup.skill cv-tailoring-setup/)
   ```

   **Windows (PowerShell):**
   ```powershell
   cd cv-tailoring
   Compress-Archive -Path .claude.ai/skills/cv-tailoring-setup -DestinationPath cv-tailoring-setup.zip
   Rename-Item cv-tailoring-setup.zip cv-tailoring-setup.skill
   ```

2. Import `cv-tailoring-setup.skill` into Claude.ai via **Customisations > Skills**
3. Start a new conversation and say "set up cv tailoring"
4. Upload your CV files when prompted and follow the setup conversation
5. At the end, download and import the personalised `cv-tailoring.skill` file

Full guide: [docs/getting-started-claude-ai.md](docs/getting-started-claude-ai.md)

---

## Using the skill

Once set up, start a new session and either:

- Paste a job description and say **"tailor a CV for this"**
- Provide a path to a `.docx` JD file (Claude Code only)

The skill runs the full tailoring process and saves the output to an organised folder named with the date, recruiter, organisation, and role type.

---

## How it works

Want to understand what's happening under the hood? Read [docs/how-it-works.md](docs/how-it-works.md) for a plain-English explanation of all the components, how they fit together, and what gets stored where.

---

## File structure

```
cv-tailoring/
├── .claude/skills/
│   ├── cv-tailoring/SKILL.md       # Main tailoring skill (Claude Code)
│   └── cv-setup/SKILL.md           # Setup skill (Claude Code)
├── .claude.ai/skills/
│   └── cv-tailoring-setup/         # Setup skill (Claude.ai)
│       ├── SKILL.md
│       └── templates/
├── docs/                           # Detailed guides and documentation
├── generate_cv.py                  # Document generator (Claude Code)
├── references/                     # Formatting specs (committed)
│   ├── document-template.md        # CV formatting specification
│   └── supporting-documents.md     # Cover letter / criteria / pitch structure
├── config.example.yaml             # Configuration template
├── config.yaml                     # Your configuration (git-ignored)
├── cv-variants/                    # Your CV files (git-ignored)
├── outputs/                        # Generated documents (git-ignored)
├── skills-log.md                   # Experience log (git-ignored)
└── references/writing-standards.md # Generated by /cv-setup — personalised, git-ignored
```

Files marked *(git-ignored)* are created locally and never committed to the repository — they contain your personal information.

---

## Prerequisites (Claude Code only)

- **Node.js 18+** — [nodejs.org](https://nodejs.org/)
- **Claude Code** — `npm install -g @anthropic-ai/claude-code`
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- **Python packages** — `pip install python-docx pyyaml`
- **Git** — [git-scm.com](https://git-scm.com/)

See [docs/getting-started-claude-code.md](docs/getting-started-claude-code.md) for detailed installation instructions for each operating system.

---

## License

MIT — see [LICENSE](LICENSE) for details.
