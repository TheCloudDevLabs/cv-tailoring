---
name: cv-tailoring
description: "Tailor {{USER_NAME}}'s CV and produce supporting documents (cover letters, selection criteria responses, pitch documents) for specific job applications. Use this skill whenever the user pastes a job description, mentions tailoring or updating a CV, says 'tailor a CV for this', asks for a cover letter or selection criteria response for a role, or references applying for a specific position. Also trigger when the user asks to review CV variants, do a gap analysis against a job ad, or produce any application document. This skill must be used for any CV or job application work, even if the user does not explicitly say 'tailor'."
---

# CV Tailoring

This skill tailors {{USER_NAME}}'s CV to specific job applications and produces supporting documents. It draws on CV variants stored in the skill files, each containing different technical details, project descriptions, and role emphases.

Before doing anything else, read `references/writing-standards.md` and `references/cv-variants.md` from this skill's directory. These contain the writing constraints and the full inventory of CV variants. All CV variants are bundled in the `cv-variants/` directory within this skill.

## File locations

All files are bundled in this skill — they do not depend on project files or uploads.

- **CV variants:** `cv-variants/` directory alongside this SKILL.md
- **References:** `references/` directory alongside this SKILL.md

To resolve paths, use the directory where this SKILL.md was loaded from as the base.

## Process

Follow these steps in order for each new application.

### Step 1. Read all CV variants

Read every CV variant listed in `references/cv-variants.md`. The variants are in `cv-variants/` within this skill. Read them all before doing anything else. After reviewing all files, identify which variant is the best starting base and note content from other variants that should be incorporated.

Do not rely on a single base CV. Experience relevant to the target role may only be documented in one or two variants.

### Step 2. Gap analysis

Compare the job requirements against the content found across all CV variants. Present the gap analysis clearly, distinguishing between:

- Content that already exists and needs repositioning or emphasis adjustment
- Genuinely undocumented experience that requires input from the user

Group the gaps logically. This sets up the question sequence in Step 3.

### Step 3. Question-driven alignment

For each gap, work through it using a structured question sequence. Address one gap at a time.

**a. Initial question.** Use a widget prompt to ask whether the user has relevant experience in the gap area.

**b. Level of experience.** Follow up to establish depth — hands-on delivery, technical oversight, advisory input, or strategic direction.

**c. Role attribution.** Ask which roles or engagements the experience was part of. List relevant roles as multi-select options.

**d. Clarification if needed.** Optional final question if framing is still ambiguous.

Move to the next gap only after the current one is fully resolved.

### Step 4. Profile and skills review

Propose changes to the profile summary and skills sections first. Confirm direction before moving to employment history.

### Step 5. Employment history

Work through each role systematically, adjusting language and emphasis to match the target without overstating experience. Draw on content from all CV variants where relevant.

### Step 6. Document generation

Produce the final CV as a downloadable .docx file. Read `references/document-template.md` for the formatting specification, then read the docx skill at `/mnt/skills/public/docx/SKILL.md` for the technical approach.

### Step 7. Supporting documents

Use a widget prompt to ask whether any additional documents are needed:

- Cover letter
- Pitch document
- Selection criteria response
- None needed

If requested, produce each as a separate .docx file using the same writing standards. Read `references/supporting-documents.md` for structure and approach.

## Widget prompt guidelines

All questions must use interactive widget prompts.

- Present one gap area at a time
- Ask initial question, level, and role attribution as separate sequential prompts
- Use short, clear option labels
- Prefer multi-select where more than one option may apply
- Use ranking prompts when order of emphasis matters
- Only use freeform prompts for genuinely open-ended inputs
- Always include a brief conversational message before presenting the widget

## Writing standards

All content must follow the standards in `references/writing-standards.md`. Read the full reference before producing any content.

{{VARIANT_LIST}}
