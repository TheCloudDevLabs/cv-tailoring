---
name: cv-tailoring-setup
description: "Set up a personalised CV tailoring skill from the user's own CV files and preferences. Use this skill whenever the user says 'set up cv tailoring', 'create my cv skill', 'initialise cv tailoring', 'build a cv tailoring skill from my CVs', uploads CV files and asks to turn them into a skill, or says 'I want to use cv-tailoring with my own CVs'. Also trigger when the user asks to create a reusable CV tailoring workflow from their documents. This skill reads the user's CV documents, collects their personal details, domain context, and writing preferences, generates a complete personalised cv-tailoring skill, and packages it as a .skill file ready for import."
---

# CV Tailoring Setup

This skill creates a personalised cv-tailoring skill from the user's own CV files and preferences. The output is a complete, ready-to-import `.skill` file that bundles the user's CV variants, personalised writing standards, and all reference documents needed for the cv-tailoring workflow.

## Prerequisites

The user must upload at least one CV file. Multiple variants produce the best results.

Supported formats: `.docx`, `.pdf`, `.md`, `.txt`

## Process

Follow these steps in order.

---

### Step 1. Collect CV files

Check `/mnt/user-data/uploads/` for uploaded files. If no CV files are present, ask the user to upload them before continuing.

List all uploaded files and use a widget prompt to confirm which ones are CV variants (the user may have uploaded other documents too). Only process the confirmed CV files.

---

### Step 2. Personal details

Use widget prompts to collect the following. If any details have already been stated in the conversation, skip those questions.

1. **Full name** — "What is your full name as it should appear on your CV?"
2. **Default professional title** — "What is your default professional title? (e.g. Solution Architect, Software Engineer, Product Manager)"
3. **Email address** — "What is your contact email?"
4. **Phone number** — "What is your contact phone number? Include your country code if relevant (e.g. +1 555 000 0000, +44 7700 000000). Leave blank to skip."
5. **Location** — "Where are you located? (e.g. London, UK or Chicago, IL or Sydney, NSW)"
6. **LinkedIn URL** — "What is your LinkedIn URL? (without https://). Leave blank to skip."
7. **GitHub URL** — "Do you have a GitHub profile to include? (e.g. github.com/yourname). Leave blank to skip."
8. **Website** — "Do you have a personal website or portfolio? Leave blank to skip."
9. **Additional personal details** — multi-select widget:

   > "Are there any additional details you'd like displayed in your CV header? These appear alongside your contact information."

   Options:
   - Security or government clearance
   - Work authorisation or visa status (e.g. "Full working rights", "US Citizen")
   - Nationality
   - Languages spoken
   - Professional registration or licence number
   - Other (I'll specify)
   - None

   For each selected option, follow up to collect the value. Combine all values into a single string separated by " | " and store as `additional_info`. If none selected, store an empty string.

---

### Step 3. Domain and industry configuration

Domain configuration drives the writing standards that get bundled with the skill. Take care here.

**Primary domains** — multi-select widget:

> "Which sectors or domains do you primarily apply for roles in?"

Options:
- Australian Government (federal)
- State or Territory Government
- Defence and intelligence
- Private sector / corporate
- Technology / software / startups
- Financial services and banking
- Healthcare and medical
- Legal
- Engineering and infrastructure
- Consulting and professional services
- Academic and research
- Other

If "Other", follow up with a freeform prompt for the description.

**Compliance and regulatory context** — ask all users:

> "Do you work in areas with specific compliance, regulatory, or certification requirements that should be reflected in how your CV is written? Select all that apply."

Options:

*Government and security:* Government cybersecurity frameworks (e.g. NIST CSF, ISO 27001, ISM, Essential Eight, Cyber Essentials) / Classified or national security environments (e.g. DISP, security vetting, controlled facilities) / Government security policy and protective security (e.g. PSPF, IRAP assessments, ASD Blueprint) / Government procurement or contract compliance

*Healthcare:* Clinical data privacy (e.g. HIPAA, GDPR health data) / Clinical governance or patient safety / Medical device or pharmaceutical regulation (e.g. FDA, TGA, CE marking)

*Financial services:* Banking and financial regulation (e.g. Basel, FCA, SEC, APRA) / Anti-money laundering compliance / Payment card security (PCI-DSS)

*Technology:* Information security certification (e.g. ISO 27001, SOC 2, Cyber Essentials) / Cloud compliance (e.g. FedRAMP, national cloud standards) / Privacy regulation (e.g. GDPR, CCPA)

*Engineering and professional:* Professional engineering registration or licensing / Industry standards bodies (e.g. ISO, IEC, ASME)

*Other:* Other compliance or regulatory context (I'll describe it) / None of the above

If "Other", follow up with a freeform prompt. Store all selected items in `domain_notes`.

**Domain terminology notes** — ask:

> "Are there specific terms, acronyms, or conventions important in your field that you'd like locked in?"

Options: "Yes, I'll add some notes", "No, the defaults are fine"

If yes, collect via freeform prompt.

---

### Step 4. Writing preferences

**Spelling convention:**

> "Which spelling convention should your documents use?"

Options: "Australian English", "UK English", "US English"

(If they selected Australian Government or State/Territory, mention that Australian English is the standard for those contexts before presenting options.)

**Tone:**

> "What tone should your CV and supporting documents use?"

Options:
- "Neutral and professional — factual, direct, no promotional language"
- "Conversational but polished — readable and warm, still professional"
- "Formal and traditional — conservative register, suits law, finance, or government"

**Banned words:**

> "Are there words or phrases you want to avoid? Common offenders: 'spearheaded', 'passionate', 'leveraged', 'cutting-edge', 'best-in-class', 'thought leader', 'innovative', 'synergy'."

Options:
- "Use the suggested defaults"
- "Add my own to the defaults"
- "I have my own list"
- "No restrictions"

If "Add my own" or "I have my own list": collect via freeform follow-up.

**Team framing:**

> "How should collaborative work be framed?"

Options:
- "Lead with my contribution, note team context where relevant"
- "Always explicitly note when work was part of a team"
- "No special handling needed"

**Target page length:**

> "What is your target CV length?"

Options: "1 page", "2 pages", "3 pages", "4 or more pages (senior or executive)", "No fixed target"

**Sections to include** — multi-select, all on by default:

> "Which sections should your CV include?"

Options: Professional summary, Core skills, Employment history, Certifications and training, Education, Publications or patents (off by default), Volunteer or community involvement (off by default)

---

### Step 5. Read and convert CV files

For each confirmed CV file:

1. If `.docx`: use python-docx to extract the text content
2. If `.pdf`: extract text using available tools
3. If `.md` or `.txt`: read directly

Produce a clean markdown version of each CV. Preserve structure (headings, sections, bullet points, employment history) but clean up conversion artefacts. Store in memory.

---

### Step 6. Analyse CV variants

Review all converted CVs and identify:

- Each variant's primary focus (e.g. "Security Architect", "Cloud Engineer")
- What makes each variant distinct (role emphasis, project details, skills highlighted)
- The user's employment history across all variants
- Certifications, clearances, or qualifications mentioned

Present a brief summary and use a widget prompt to confirm the variant names and focus areas are correct before proceeding.

---

### Step 7. Generate the skill

Create the cv-tailoring skill folder at `/home/claude/cv-tailoring/` with this structure:

```
cv-tailoring/
├── SKILL.md
├── cv-variants/
│   └── [Name]_[Variant_Focus].md   (one per CV variant)
└── references/
    ├── cv-variants.md
    ├── writing-standards.md
    ├── document-template.md
    └── supporting-documents.md
```

#### SKILL.md

Read the template at `templates/skill-template.md` in this skill's directory. Replace all placeholders with the user's actual values:

- `{{USER_NAME}}` → the user's full name
- `{{VARIANT_LIST}}` → list of CV variant filenames generated in this run

#### CV variant files

Save each converted CV as a markdown file in `cv-variants/`. Name convention: `[Surname]_[GivenName]_[Variant_Focus].md` (e.g. `Smith_Jane_Security_Architect.md`).

#### references/cv-variants.md

Read the template at `templates/cv-variants-template.md`. Replace `{{VARIANT_INVENTORY}}` with an entry for each variant:

```
### [filename.md]
[One to two sentence description of the variant's primary focus and what distinguishes it from others.]
```

#### references/writing-standards.md

Generate this file from scratch based on the configuration collected in Steps 3 and 4. Do not copy the generic template — this must be personalised to the user's domain, spelling, tone, and banned words.

Structure and generate each section as follows. Where the user has not explicitly configured something, use intelligent defaults based on their domain context.

**Tone and language section:**
Write based on the spelling convention (with concrete spelling examples for the chosen convention), the selected tone, and the banned words list. If Australian or UK English: give examples (organisation, programme, licence as noun, practise as verb). Include the full banned words list.

**Accuracy section:**
Write based on the team framing preference. Always include: do not overstate experience, seniority, or involvement; do not claim qualifications not held; descriptions must reflect what was actually done.

**Domain-specific terminology section:**
Generate one subsection per domain selected. Use the reference below. Do not generate sections for domains not selected. Fill in standard conventions for anything the user left unconfigured.

> **Technology / software / startups:** Name specific technologies, versions, approaches. Distinguish generalism from deep technical ownership. Quantify scale (users, requests/second, data volume, cost). Name specific cloud provider and service — avoid vague "cloud" references.

> **Private sector / corporate:** Commercial language acceptable, avoid buzzwords. P&L, ARR, cost reduction language appropriate for senior roles. Quantify outcomes. Prefer specific stakeholder level names over generic "stakeholder management".

> **Financial services and banking:** Reference APRA, ASIC, AML/CTF where relevant. Risk language (operational risk, residual risk, control effectiveness) is standard. Distinguish BAU from project/change work. Use entity-specific language (bank, insurer, superannuation fund). Reference CDR and Privacy Act with precision.

> **Consulting and professional services:** Quantify client engagements (number, size, sector). Distinguish strategy, advisory, implementation, managed service. Note level of practice with frameworks (TOGAF, ITIL, PRINCE2, Agile/SAFe), not just awareness.

> **Healthcare and medical:** Use precise clinical terms. Regulatory bodies: TGA, AHPRA. Health data standards: My Health Record, FHIR, HL7 — spell out on first use. Privacy: Health Records Act, APPs. "Patient outcomes" and "clinical safety" are high-value phrases.

> **Legal:** Precision paramount — do not use synonyms for legal terms. Distinguish advising, appearing, drafting, negotiating. Note jurisdiction and area of law. Formal register throughout.

> **Engineering and infrastructure:** Reference AS/NZS and ISO standards. Note Engineers Australia membership and CPEng/MIEAust if held. Distinguish design, specification, delivery, commissioning. Quantify project value and scale.

> **Academic and research:** Publication citations: distinguish peer-reviewed from other outputs. Grants: name funding body, amount, and role (CI, co-CI). Teaching: distinguish undergraduate, postgraduate, supervision, coordination. Note impact indicators where measurable.

> **Australian Government:** Security classifications: PROTECTED, SECRET, TOP SECRET (all caps, no quotes). Frameworks: ISM, PSPF, Essential Eight (capitalised, no hyphen), ASD Blueprint for Secure Cloud. Agencies: ASD, ACSC, DISP. Use "Australian Government" not "Federal Government". IRAP — spell out on first use. Accreditation: "IRAP assessment", "accreditation" (not "certification" for systems), "Authority to Operate (ATO)". Essential Eight maturity levels: Maturity Level 0, 1, 2, 3.
> **State or Territory Government:** Use correct jurisdiction name (e.g. "ACT Government", not "State Government"). ICT preferred over IT. Apply federal classification conventions if security context applies. Reference relevant state digital strategy where applicable.

> **Defence and intelligence:** DISP — reference precisely. AGSVA handles personnel vetting — do not conflate with IRAP. Agencies: ADF, DIO, DSTG. Clearance levels: Baseline, NV1, NV2, PV — use these exact terms. Use "capability" not "feature". Do not use US military terminology unless the role explicitly relates to that context.

**Formatting constraints section:**
Always include regardless of domain:
- Headings must stand alone
- No dot-point blurbs under headings — use full paragraphs or full bullet lists
- No em dash overuse — prefer commas or parentheses
- No decorative formatting
- Consistent heading levels throughout
- No redundant structural elements
- Never reference source CV documents

**CV-specific rules section:**
Write based on selected sections and target page length. If 1–2 pages: concision is critical; older roles summarised or omitted; bullets kept tight. If 3 pages: standard depth; roles beyond 10 years summarised. If 4+: extended descriptions appropriate. Always: summary as coherent paragraphs (not claim lists); employment history uses intro paragraph + bullets for deliverables; vary framing across roles to show progression; remove irrelevant skills; do not pad.

**Supporting document rules:**
Always include: cover letters — one page, directly address role requirements, do not restate CV, do not open with "I am writing to apply for..."; selection criteria — narrative format, specific examples, each response self-contained, three to five paragraphs per criterion; pitch documents — clear value proposition, no generic statements, useful for contract roles.

#### references/document-template.md

Copy directly from `templates/document-template.md` in this skill's directory.

#### references/supporting-documents.md

Copy directly from `templates/supporting-documents.md` in this skill's directory.

---

### Step 8. Package and deliver

Package the generated skill folder as a `.skill` file:

```bash
cd /home/claude
zip -r /home/claude/cv-tailoring.skill cv-tailoring/
```

Copy to `/mnt/user-data/outputs/` and present the file to the user.

Present a summary:
- Number of CV variants bundled
- The variant names and focus areas
- Their configured domains and writing preferences
- Instructions: drag the `.skill` file into Claude's skill settings to import

---

### Step 9. Optional — next steps

After delivering the skill, use a widget prompt to ask if the user wants to:

- Run a test tailoring session with a sample job description
- Make changes to any generated files
- Add more CV variants (re-run this setup)

---

## File locations

All templates are in the `templates/` directory within this skill folder, at the same level as this SKILL.md.

## Error handling

If a CV file cannot be read (corrupted, password-protected, unsupported format), notify the user and continue with the remaining files. At least one CV must be successfully processed to generate the skill.
