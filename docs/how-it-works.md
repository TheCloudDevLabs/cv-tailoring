# How It Works

This document explains all the components of the CV tailoring skill — what each part does, how they connect, and why it works the way it does. You don't need to read this to use the skill, but it's useful if you're curious, want to customise something, or want to understand what's happening during a session.

---

## The core idea

Most people applying for jobs have more than one version of their CV. One might be written for architecture roles, another for security roles, another from when they applied as a consultant. Each version has slightly different language, different emphasis, and sometimes different project details.

The problem is that no single variant covers everything. The architecture CV might have a detailed project narrative that didn't make it into the security CV. The consulting CV might describe a role in a way that's relevant to a new opportunity but not in the most obvious version.

This skill reads all your CV variants before doing anything, so it can draw on the full breadth of what you've documented. It then analyses the job description, identifies what needs to change, asks you targeted questions to fill any genuine gaps, and produces a tailored version.

The questions are structured so you're always choosing from options or answering direct questions — not writing anything from scratch.

---

## Components

### The setup skill

Before you can tailor a CV, you run setup once. Setup collects:

- **Your personal details** — name, contact information, LinkedIn, GitHub, clearance level
- **Your domain context** — which sectors you work in (government, technology, healthcare, etc.)
- **Your writing preferences** — spelling convention, tone, words to avoid, how to frame collaborative work
- **Your CV files** — the source documents the tailoring skill draws from

Setup generates three things from this information:

1. `config.yaml` — a configuration file with your personal details and settings
2. `references/writing-standards.md` — a personalised set of writing rules tailored to your domain
3. `references/cv-variants.md` — an inventory of your CV variants with a short description of each

These three files are what the tailoring skill reads at the start of every session.

### The tailoring skill

The tailoring skill runs every time you want to tailor a CV for a specific role. It follows a fixed sequence:

1. Reads `config.yaml`, `writing-standards.md`, and `cv-variants.md`
2. Reads every CV variant
3. Analyses the job description against what's in the variants
4. Works through gaps using structured questions
5. Proposes a new profile and skills section
6. Works through the employment history role by role
7. Generates the output document(s)

### The CV variants

CV variants are the source material. They're stored as Markdown files (`.md`) in the `cv-variants/` folder. If you provided `.docx` files during setup, they were automatically converted to Markdown — the originals are preserved in `cv-variants/originals/`.

Markdown is used instead of Word format because it's faster for Claude to read and process. The content is identical.

You can have as many variants as you like. There's no requirement that they cover different roles — you might just have multiple versions from different points in your career. The skill reads them all and pulls in whatever's relevant.

### The skills log (Claude Code only)

The skills log (`skills-log.md`) is a running record of experience that comes up during tailoring sessions but isn't documented in any of your CV variants.

For example: during a tailoring session, you might mention that you led a compliance audit at a particular organisation. If that's not in any of your CV files, the skill logs it automatically. In future sessions, if a role requires that experience, the skill will surface that log entry and ask if you want to include it — rather than asking you to describe it from scratch again.

This means the skill gets more useful over time as your log grows. The CV variants remain the source of truth; the skills log is a supplement.

### The writing standards

`references/writing-standards.md` defines how all generated content should be written. It's generated during setup based on your domain configuration and preferences.

It covers:

- **Tone and language** — spelling convention, banned words, level of formality
- **Accuracy** — how to attribute collaborative work, what not to overstate
- **Domain-specific terminology** — sector-appropriate conventions. For Australian Government roles: classification markings, ISM/PSPF/Essential Eight conventions, agency abbreviations. For technology roles: naming specific cloud providers and services rather than generic "cloud". For financial services: regulatory framework references. And so on for each domain you selected.
- **Formatting rules** — what not to do (decorative formatting, mixed paragraph and bullet structures, etc.)
- **CV-specific rules** — profile format, employment history structure, how to handle page length
- **Supporting document rules** — cover letter, selection criteria, and pitch document conventions

A "Custom overrides" section at the bottom of the file is never touched by setup — anything you add there manually will survive if you re-run setup.

### The config file

`config.yaml` stores your personal details and system paths. The tailoring skill reads it at the start of every session to populate the header of your generated CV (name, title, contact, LinkedIn, clearance).

The config also defines where your files live. If you want your CV variants or outputs in a different folder, you can change the paths in the config rather than moving the actual files.

`config.example.yaml` is the template committed to the repository. Your personal `config.yaml` is never committed — it's listed in `.gitignore`.

### The document generator (Claude Code only)

`generate_cv.py` is a Python module that produces the formatted `.docx` file. The tailoring skill builds a structured content dictionary (name, title, contact details, summary paragraphs, skills, employment history, certifications) and passes it to this module, which handles all the Word formatting.

This approach keeps the document formatting consistent and separates it from the AI's job, which is generating the content. You don't need to interact with this file directly.

For Claude.ai, Claude generates the formatted `.docx` file directly and presents it as a downloadable attachment within the conversation.

---

## The tailoring process in detail

### Gap analysis

After reading all CV variants, the skill compares the job description against what's documented. It distinguishes between:

- **Covered content** — experience that exists in your CVs but may need repositioning or different emphasis for this role
- **Underdocumented content** — experience that exists but is buried, mentioned only briefly, or framed for a different context
- **Genuine gaps** — areas where you either don't have the experience, or haven't documented it yet

The gap analysis is presented before any questions are asked, so you can see the full picture first.

### Question sequence

For each gap, the skill follows a structured sequence:

1. **Do you have experience in this area?** — Simple yes/no or options for the type/nature of experience
2. **At what level?** — Hands-on delivery, technical oversight, advisory input, or strategic direction
3. **Which roles did it relate to?** — Multi-select from your employment history
4. **Any clarification needed?** — Optional final question if the framing is still ambiguous

This sequence is designed to produce content that's accurate and attributable to the right roles. It avoids you having to write anything — you describe; Claude writes.

### New experience gets logged

If your answers reveal experience that isn't documented in any CV variant, the skill adds an entry to the skills log automatically. This happens silently — you don't need to approve it.

Each log entry records:
- The skill or experience area
- A precise description of what you said
- Which roles it applies to
- The date and what type of application it was logged during

### Output structure

Generated files go into a subfolder under `outputs/`, named with the date, recruiter, organisation, and role type:

```
outputs/YYYY-MM-DD_Recruiter_Org_RoleType/
├── Your_Name_Role_Type.docx    # The tailored CV
└── JD_Org_RoleType.txt         # The job description (archived)
```

If you provided the JD as a Word file, the original is also copied into the folder.

The tailored CV content is also saved as a Markdown file in `cv-variants/` — it becomes part of your library of variants for future sessions.

---

## Writing standards in practice

Here are a few concrete examples of how writing standards affect the output.

**Banned words** — if "spearheaded" is in your banned list and Claude drafts "spearheaded the migration", it will rewrite to something like "led the migration" or "delivered the migration".

**Domain terminology** — if you selected financial services, the skill uses precise regulatory language ("APRA-regulated environment", "operational risk framework") rather than generic alternatives. If you selected technology, it names specific cloud providers and services rather than writing "cloud infrastructure".

**Team framing** — if you selected "lead with my contribution, note team context where relevant", a bullet might read: "Designed and delivered the data pipeline architecture, working alongside the platform and security teams to align with existing standards." Rather than either claiming sole ownership or burying your contribution in a team description.

**Page length target** — if you selected 2 pages, the skill keeps bullet points concise and won't include extended role descriptions for positions more than 8 years ago.

---

## Customising the writing standards

The easiest way to customise your writing standards is to re-run setup and change your preferences — the file gets regenerated.

If you want to make fine-grained changes that the setup questions don't cover, open `references/writing-standards.md` in any text editor and add rules to the **Custom overrides** section at the bottom. This section is preserved when you re-run setup, so your manual additions won't be overwritten.

Examples of custom overrides:

```markdown
## Custom overrides

- Always write out "machine learning" in full — do not abbreviate to "ML" in client-facing documents.
- Do not use "architect" as a verb (e.g. "architected the solution").
- When describing technical roles, lead with the business outcome before the technical approach.
```

---

## Privacy and data

**Claude Code:** Your CV content, config, and generated files live entirely on your computer. They are sent to Claude's API when you run a session (Claude needs to read your files to work with them), but nothing is stored by Anthropic beyond normal API logging. Files marked as git-ignored (`config.yaml`, `cv-variants/`, `outputs/`, `skills-log.md`) are never committed to the repository.

**Claude.ai:** Your CV content is bundled into the `.skill` file on your device. When you use the skill in a conversation, the CV content is sent to Claude as part of that conversation. See [Anthropic's privacy policy](https://anthropic.com/privacy) for how conversation content is handled.

In both cases, your CV files are never shared with third parties or used to train AI models under Anthropic's standard API and consumer product terms.

---

## File reference

| File | What it is | Git-ignored? |
|---|---|---|
| `config.yaml` | Your personal configuration | Yes |
| `config.example.yaml` | Template — copy to config.yaml | No |
| `references/writing-standards.md` | Personalised writing rules, generated by setup | Yes |
| `references/cv-variants.md` | CV variant inventory, generated by setup | Yes |
| `references/document-template.md` | CV formatting specification | No |
| `references/supporting-documents.md` | Cover letter / criteria / pitch structure | No |
| `cv-variants/` | Your CV files (Markdown and originals) | Yes |
| `skills-log.md` | Running log of undocumented experience | Yes |
| `outputs/` | Generated documents | Yes |
| `jds/` | Job description files | Yes |
| `generate_cv.py` | Word document generator (Claude Code) | No |
| `.claude/skills/cv-tailoring/` | Tailoring skill (Claude Code) | No |
| `.claude/skills/cv-setup/` | Setup skill (Claude Code) | No |
| `.claude.ai/skills/cv-tailoring-setup/` | Setup skill (Claude.ai) | No |

"Git-ignored" means the file is listed in `.gitignore` and will never be committed to the repository if you clone or fork this project. This protects your personal information from being accidentally published.
