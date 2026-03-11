---
name: cv-tailoring
description: "Tailor your CV and produce supporting documents (cover letters, selection criteria responses, pitch documents) for specific job applications. Use this skill whenever you paste a job description, mention tailoring or updating a CV, ask for a cover letter or selection criteria response, or reference applying for a specific position."
---

# CV Tailoring

This skill tailors your CV to specific job applications and produces supporting documents. It draws on a set of CV variants stored in the project, each containing different technical details, project descriptions, and role emphases.

Before doing anything else, read `config.yaml` from the project root, then read `references/writing-standards.md` and `references/cv-variants.md`. These contain your personal configuration, writing constraints, and the full inventory of CV variants you need to work from.

## Trigger

The user provides a job description — either by pasting it as text, by supplying a path to a `.docx` file, or by providing a URL to a job listing — and says something like "tailor a CV for this." If the role has a specific emphasis not obvious from the title (for example, a Solution Architect role that is primarily governance-focused), the user may flag that alongside the job description.

## File locations

All paths are resolved relative to the project root (the directory containing `config.yaml`).

- **Config file:** `config.yaml` in the project root (created by /cv-setup)
- **Reference files:** `references/` directory in the project root
- **CV variants:** Path specified in `config.yaml` under `paths.cv_variants` (default: `cv-variants/`)
- **Skills log:** Path specified in `config.yaml` under `paths.skills_log` (default: `skills-log.md`)
- **Outputs:** Path specified in `config.yaml` under `paths.outputs` (default: `outputs/`)
- **Generator module:** `generate_cv.py` in the project root

## Pre-flight check

At the start of every tailoring session, verify that `config.yaml` exists and contains the required personal details. If it is missing or incomplete, tell the user to run `/cv-setup` first.

Load the config using Bash:

```bash
python3 -c "
import yaml
with open('config.yaml') as f:
    config = yaml.safe_load(f)
p = config['personal']
print(f'Name: {p[\"name\"]}')
print(f'Email: {p[\"email\"]}')
print(f'Configured: {bool(p[\"name\"] and p[\"email\"])}')
"
```

If the name or email is empty, prompt the user to run `/cv-setup`.

## Process

Follow these steps in order for each new application.

### Step 0. Extract JD text

If the user has provided a URL, extract the JD using WebFetch:

```
WebFetch(url=<the URL>, prompt="Extract the full job description including role title, responsibilities, requirements, and selection criteria. Return the complete text without summarising.")
```

Store the result as the working JD for all subsequent steps.

If the user has provided a file path to a `.docx` file rather than pasting text, extract the full text. Use this bash command:

```bash
python3 -c "
from docx import Document
doc = Document('/path/to/jd.docx')
text = []
for element in doc.element.body:
    if element.tag.endswith('}p'):
        t = ''.join((r.text or '') for r in element.iter() if r.tag.endswith('}t'))
        if t.strip():
            text.append(t)
    elif element.tag.endswith('}tbl'):
        for row in element.iter():
            if row.tag.endswith('}tr'):
                cells = []
                for cell in row:
                    if cell.tag.endswith('}tc'):
                        cells.append(''.join((r.text or '') for r in cell.iter() if r.tag.endswith('}t')))
                if any(c.strip() for c in cells):
                    text.append(' | '.join(cells))
print('\n'.join(text))
"
```

Replace `/path/to/jd.docx` with the actual path the user supplied. If `python-docx` is not available, fall back to:

```bash
pandoc --to plain /path/to/jd.docx
```

If the user pasted text directly, use it as-is.

Store the extracted text as the working JD for all subsequent steps. If a `.docx` was provided and neither extraction tool is available, ask the user to paste the text directly.

### Step 1. Read config and all CV variants

First, read `config.yaml` from the project root. This contains the user's personal details and path configuration.

Then read `references/writing-standards.md` and `references/cv-variants.md` from the project root.

Read every CV variant listed in `references/cv-variants.md`. The variants are in the directory specified by `paths.cv_variants` in the config (default: `cv-variants/`). Read them using the `Read` tool. Each variant contains content that may not appear in others. After reviewing all files, identify which variant is the best starting base and note any additional content from other variants that should be incorporated.

Do not rely on a single base CV. Experience relevant to the target role may only be documented in one or two variants.

After reading all CV variants, read the skills log from the path specified in `paths.skills_log` (default: `skills-log.md`) if it exists. Parse all entries — each entry records experience discovered in a previous session that is not yet in any variant file. These entries are available for use during gap analysis and questioning in this session.

### Step 2. Gap analysis

Compare the job requirements against the content found across all CV variants. Present the gap analysis clearly, distinguishing between:

- Content that already exists and needs repositioning or emphasis adjustment
- Genuinely undocumented experience that requires input from the user

Group the gaps logically. This analysis sets up the question sequence in the next step.

### Step 3. Question-driven alignment

For each gap or underdocumented area identified in the analysis, work through it using a structured question sequence. Address one gap at a time. Do not batch questions across multiple gap areas.

Before beginning the question sequence for each gap, check whether any skills log entries are relevant to that gap area. If a relevant entry exists, surface it to the user using an `AskUserQuestion` prompt before asking about their experience from scratch. The prompt must:

- Identify the specific log entry (skill area and short descriptor)
- Name the roles the experience was previously attributed to
- Quote or paraphrase the JD requirement it aligns with
- Offer clear options: include it in this section, place it elsewhere in the CV, or skip it for this application

Only proceed to the standard question sequence if no relevant log entry exists, or if the user has chosen to skip the logged entry.

For each gap, follow this sequence:

**a. Initial question.** Use an `AskUserQuestion` prompt to ask whether the user has relevant experience in the gap area. Offer clear options such as the type or nature of the experience, or a simple yes/no where appropriate.

**b. Level of experience.** Once confirmed, follow up with an `AskUserQuestion` prompt to establish depth. Distinguish between levels such as hands-on delivery, technical oversight, advisory input, or strategic direction. Use single-select with clear labels.

**c. Role attribution.** Ask which roles or engagements the experience was part of. List relevant roles from the employment history as multi-select options so the experience can be attributed to the correct positions.

**d. Clarification if needed.** If the answers leave ambiguity about how to represent the experience, ask a final targeted question before writing. This step is optional.

**e. Log any new experience.** If the user's answers reveal experience that is not documented in any CV variant or existing skills log entry, immediately append a new entry to the skills log before moving to the next gap. Use this format:

```markdown
## YYYY-MM-DD | [Skill/Experience Area] | [Short descriptor]
- Roles: [Role Title @ Org for each applicable role]
- Detail: [Technically precise description of the experience as stated by the user]
- Logged during: [Target role type] application, [Month Year]
```

Do not ask the user to confirm the log entry — write it silently as part of closing out the gap.

Move to the next gap only after the current one is fully resolved.

### Step 4. Profile and skills review

Propose changes to the profile summary and skills sections first. Present the proposed direction and confirm before moving to employment history.

### Step 5. Employment history

Work through each role systematically, adjusting language and emphasis to match the target without overstating experience. Draw on content from all CV variants where relevant, not just the base document.

Each role must use a brief intro paragraph (one to two sentences of context) followed by bullet points for specific deliverables. Do not use narrative paragraphs for the deliverables.

### Step 6. Document generation

Before generating the .docx, ask for the recruiter's name if it has not already been provided. It is required for the output folder name.

Produce the final CV as a .docx file using the centralised generator module. Write a short Python script that:

1. Reads `config.yaml` to get personal details
2. Imports `generate_cv` from `generate_cv`
3. Builds a content dict following the schema below, populating personal fields from config
4. Calls `generate_cv(content, output_path)`

Execute the script via Bash.

The content dict schema:

```python
{
    "name": str,              # From config.yaml personal.name
    "title": str,             # Role-specific title for this application
    "contact": {
        "email": str,         # From config.yaml personal.email
        "phone": str,         # From config.yaml personal.phone
        "location": str,      # From config.yaml personal.location
    },
    "linkedin": str,          # From config.yaml personal.linkedin (can be empty)
    "additional_info": str,   # From config.yaml personal.additional_info (can be empty)
    "summary": [str, ...],    # List of paragraphs
    "core_skills": str,       # "Skill A · Skill B · Skill C"
    "roles": [
        {
            "title": str,     # "Solution Architect"
            "org": str,       # "Company (Client)"
            "dates": str,     # "August 2024 – Present"
            "intro": str,     # Brief intro paragraph (optional, can be "")
            "bullets": [str]  # List of bullet point strings
        },
    ],
    "certifications": [str],
    "courses": [str],         # Optional, can be omitted or empty
}
```

Example generation script structure:

```python
import sys, yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

sys.path.insert(0, ".")
from generate_cv import generate_cv

content = {
    "name": config["personal"]["name"],
    "title": "...",  # Role-specific title
    "contact": {
        "email": config["personal"]["email"],
        "phone": config["personal"]["phone"],
        "location": config["personal"]["location"],
    },
    "linkedin": config["personal"].get("linkedin", ""),
    "additional_info": config["personal"].get("additional_info", ""),
    # ... rest of content built from tailoring process
}

output_path = "outputs/YYYY-MM-DD_Recruiter_Org_RoleType/Name_Title.docx"
generate_cv(content, output_path)
```

Do not write any python-docx formatting code in the generation script. The module handles all formatting internally.

#### Output folder

All generated files must be written to a dedicated subfolder under the configured outputs path (default: `outputs/` in the project root). The subfolder name follows this convention:

```
YYYY-MM-DD_Recruiter_Org_RoleType
```

For example: `2026-03-03_RecruiterName_OrgShortName_Solution_Architect`

- `YYYY-MM-DD` is today's date
- `Recruiter` is the recruiter's name or agency (ask if not known)
- `Org` is a short identifier for the hiring organisation
- `RoleType` is the role title in PascalCase with underscores

Each output folder must contain:
1. The generated `.docx` CV file
2. A `JD_[Org]_[RoleType].txt` file containing the full job description text and any recruiter context notes provided
3. If the JD was supplied as a `.docx` file, also copy the original file into the output folder as `JD_[Org]_[RoleType]_original.docx`

Do not save generated .docx files to the project root.

#### Output confirmation

After the generation script completes successfully, present a clear summary to the user listing every file created in the output folder. Use this format:

> **CV generated successfully.** The following files have been saved to `outputs/[folder name]/`:
>
> - `Name_Title.docx` — Tailored CV
> - `JD_Org_RoleType.txt` — Job description text
> - `JD_Org_RoleType_original.docx` — Original JD file *(only if a .docx JD was provided)*

Include the full relative path for each file. If the generation script fails, report the error clearly and do not proceed to the variant archive step.

#### CV variant archive

After generating the .docx file, also save the final tailored CV content as a Markdown file in the `cv-variants/` directory. Use the naming convention:

```
[Name]_[Role Type]_[Org or Context].md
```

Where `[Name]` uses the user's name from config with spaces replaced by underscores. For example: `Jane_Smith_Cloud_Security_Lead_GovAgency.md`.

If the role type is already represented by an existing variant with no meaningful new framing, save it as a dated variant:

```
[Name]_[Role Type]_[YYYY-MM].md
```

This preserves the tailored content as a source-of-truth variant for future sessions to draw on.

#### Update variant index

After saving the new variant, use an `AskUserQuestion` prompt:

> "A new CV variant was saved to `cv-variants/`. Would you like to update the variant index?"
>
> **Yes** — The new variant will be included in future tailoring sessions. Its content will be available during gap analysis and can be drawn on when building CVs for similar roles.
>
> **No** — The variant file is still saved, but future sessions won't know it exists. Content from this variant won't be considered during gap analysis.

If yes:

1. Read the newly saved variant `.md` file
2. Generate a one to two sentence description of its focus and emphasis
3. Append a new entry to `references/cv-variants.md` under the `## Variant inventory` section:

```markdown
### [variant-filename.md]
[One to two sentence description of the variant's focus and emphasis.]
```

### Step 7. Supporting documents

Once the CV is complete, use an `AskUserQuestion` prompt to ask whether any additional documents are needed. Offer these options:

- Cover letter
- Pitch document
- Selection criteria response
- None needed

If a supporting document is requested, produce it as a separate .docx file using the same writing standards and tailored to the same role. Read `references/supporting-documents.md` for the structure of each document type.

## AskUserQuestion guidelines

All questions during the tailoring process must use the `AskUserQuestion` tool. This keeps the process structured and reduces ambiguity.

- Present one gap area at a time. Do not combine questions about different gap areas into a single widget.
- Within a single gap area, the initial question, level of experience, and role attribution should be asked as separate sequential prompts. Do not combine all three into one widget.
- Use short, clear option labels. Add descriptions only when the choice is not self-explanatory.
- Prefer multi-select over single-select where more than one option may apply.
- When asking which roles an experience relates to, list the relevant roles from the employment history as selectable options.
- Use ranking prompts when the order of emphasis matters (for example, which capability areas to lead with in the profile).
- Only use prose questions for genuinely open-ended inputs such as project descriptions, specific technical details, or organisational context that cannot be reduced to selectable options.
- Always include a brief conversational message before presenting the widget.

## Decisions requiring user input

Some decisions cannot be made without confirmation. Flag these using `AskUserQuestion` prompts rather than assuming:

- Whether a requirement is something that can be legitimately claimed based on actual experience
- How to frame experience that partially matches a requirement
- Any role-specific context, such as knowledge of the hiring organisation or team

## Writing standards

All content produced through this process must follow the standards defined in `references/writing-standards.md`. Read the full writing standards reference before producing any content.
