---
name: cv-setup
description: "Interactive setup for the CV tailoring skill. Run this when you first clone the repo or when you want to update your configuration. Collects personal details, domain configuration, and writing preferences, then generates all reference files from scratch. Trigger when the user runs /cv-setup, asks to set up or configure the CV tailoring skill, or wants to update their personal details or preferences."
---

# CV Setup

Interactive onboarding for the CV tailoring skill. Generates `config.yaml`, `references/writing-standards.md`, and `references/cv-variants.md` from scratch. After running this, the cv-tailoring skill has everything it needs.

## Pre-flight check

Check whether `config.yaml` exists in the project root.

- If it exists, read it and use an `AskUserQuestion` prompt to ask what they want to update: personal details, domain configuration, writing preferences, CV ingestion, or everything. Skip to the relevant step.
- If it does not exist, run the full setup flow from Step 1.

Check that Python dependencies are available:

```bash
python3 -c "import docx; import yaml; print('OK')"
```

If missing, tell the user to run: `pip install python-docx pyyaml`

Also create `references/` if it does not exist:

```bash
mkdir -p references
```

## Step 1: Personal details

Ask one field at a time using `AskUserQuestion` open-ended prompts.

1. **Full name** — "What is your full name as it should appear on your CV?"
2. **Default professional title** — "What is your default professional title? (e.g. Solution Architect, Software Engineer, Product Manager)"
3. **Email address** — "What is your contact email address?"
4. **Phone number** — "What is your contact phone number? Include your country code if relevant (e.g. +1 555 000 0000, +44 7700 000000). Leave blank to skip."
5. **Location** — "Where are you located? (e.g. London, UK or Chicago, IL or Sydney, NSW)"
6. **LinkedIn URL** — "What is your LinkedIn URL? (without https://, e.g. linkedin.com/in/yourname). Leave blank to skip."
7. **GitHub URL** — "Do you have a GitHub profile you'd like to include? (e.g. github.com/yourname). Leave blank to skip."
8. **Website** — "Do you have a personal website or portfolio? Leave blank to skip."
9. **Additional personal details** — use an `AskUserQuestion` multi-select prompt:

   > "Are there any additional details you'd like displayed in your CV header? These appear alongside your contact information."

   Options:
   - Security or government clearance
   - Work authorisation or visa status (e.g. "Full working rights", "US Citizen")
   - Nationality
   - Languages spoken
   - Professional registration or licence number
   - Other (I'll specify)
   - None

   For each selected option, follow up with an open-ended question to collect the value (e.g. "What is your clearance level?", "What is your work authorisation status?"). Combine all collected values into a single string separated by " | " and store it as `additional_info` in the config. If "None" or nothing selected, store an empty string.

## Step 2: Domain and industry configuration

Domain configuration drives the entire writing-standards output. Work through this carefully.

### Primary domains

Use an `AskUserQuestion` multi-select prompt:

> "Which sectors or domains do you primarily apply for roles in? Select all that apply."

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

If "Other" is selected, follow up with an open-ended question to collect the description.

### Compliance and regulatory context

Ask all users:

> "Do you work in areas with specific compliance, regulatory, or certification requirements that should be reflected in how your CV is written? Select all that apply."

Options:

*Government and security*
- Government cybersecurity frameworks (e.g. NIST CSF, ISO 27001, ISM, Essential Eight, Cyber Essentials)
- Classified or national security environments (e.g. DISP, security vetting, controlled facilities)
- Government security policy and protective security (e.g. PSPF, IRAP assessments, ASD Blueprint)
- Government procurement or contract compliance

*Healthcare*
- Clinical data privacy (e.g. HIPAA, GDPR health data, local health records law)
- Clinical governance or patient safety standards
- Medical device or pharmaceutical regulation (e.g. FDA, TGA, CE marking)

*Financial services*
- Banking and financial regulation (e.g. Basel, FCA, SEC, APRA)
- Anti-money laundering and financial crime compliance
- Payment card security (PCI-DSS)

*Technology*
- Information security certification (e.g. ISO 27001, SOC 2, Cyber Essentials)
- Cloud compliance frameworks (e.g. FedRAMP, StateRAMP, national cloud standards)
- Privacy regulation (e.g. GDPR, CCPA, PDPA)

*Engineering and professional*
- Professional engineering registration or licensing
- Industry standards bodies (e.g. ISO, IEC, ASME, AS/NZS)

*Other*
- Other compliance or regulatory context (I'll describe it)
- None of the above

If "Other" is selected, follow up with a freeform open-ended question to collect the description. Store all selected items (plus any freeform description) in `domain_notes` in the config. The agent uses these to generate appropriate terminology standards in writing-standards.md.

### Domain terminology notes

Ask:

> "Are there specific terms, acronyms, or conventions important in your field that you'd like to lock in? (e.g. organisation names, framework names, product names, unusual role titles)"

Options: "Yes, I'll add some notes", "No, the defaults are fine"

If yes, collect as a freeform open-ended response.

## Step 3: Writing preferences

### Spelling convention

> "Which spelling convention should your documents use?"

Options: "Australian English", "UK English", "US English"

If the user selected Australian Government or State/Territory Government as a domain, mention that Australian English is the standard for those contexts before presenting the options.

### Tone

> "What tone should your CV and supporting documents use?"

Options:
- "Neutral and professional — factual, direct, no promotional language"
- "Conversational but polished — readable and warm, still professional"
- "Formal and traditional — conservative register, suits law, finance, or government"

### Banned words

> "Are there words or phrases you want to avoid? Common offenders: 'spearheaded', 'passionate', 'leveraged', 'cutting-edge', 'best-in-class', 'thought leader', 'innovative', 'synergy'."

Options:
- "Use the suggested defaults"
- "Add my own to the defaults"
- "I have my own list entirely"
- "No restrictions"

If "Add my own" or "I have my own list": collect additions via an open-ended follow-up.

### Team framing

> "How should collaborative work be framed?"

Options:
- "Lead with my contribution, note team context where relevant"
- "Always explicitly note when work was part of a team"
- "No special handling needed"

## Step 4: CV shape

### Target page length

> "What is your target CV length?"

Options: "1 page", "2 pages", "3 pages", "4 or more pages (senior or executive)", "No fixed target"

### Sections to include

Use an `AskUserQuestion` multi-select prompt with all options selected by default:

> "Which sections should your CV include?"

Options (all selected by default unless noted):
- Professional summary / profile
- Core skills
- Employment history
- Certifications and training
- Education
- Publications or patents (deselected by default)
- Volunteer or community involvement (deselected by default)

## Step 5: CV ingestion

Create the cv-variants directory if it does not exist:

```bash
mkdir -p cv-variants
```

Use an `AskUserQuestion` prompt:

> "Please place your existing CV files (.docx or .md) into the `cv-variants/` directory. These are the source documents the skill draws from when tailoring your CV. You can add multiple variants with different emphases. Let me know when your files are ready."

Options: "Files are ready", "I'll add them later", "I don't have any yet"

If "Files are ready":

1. Scan the directory and present all `.docx` and `.md` files in a multi-select `AskUserQuestion` prompt asking which ones are CV variants. Ignore non-CV files silently.

2. For each confirmed `.docx` CV, convert to Markdown:

```bash
python3 -c "
from docx import Document
doc = Document('cv-variants/FILENAME.docx')
text = '\n\n'.join(p.text for p in doc.paragraphs if p.text.strip())
with open('cv-variants/FILENAME.md', 'w') as f:
    f.write(text)
print('Converted: FILENAME.docx -> FILENAME.md')
"
```

Fall back to pandoc if python-docx is unavailable:

```bash
pandoc --to markdown cv-variants/FILENAME.docx -o cv-variants/FILENAME.md
```

After conversion, move originals to `cv-variants/originals/`:

```bash
mkdir -p cv-variants/originals
mv cv-variants/FILENAME.docx cv-variants/originals/
```

3. Read each `.md` CV variant using the Read tool. Generate a one to two sentence description for each.

4. Write `references/cv-variants.md`:

```markdown
# CV Variants

Auto-generated inventory of CV variants. Updated by /cv-setup.

## Variant inventory

### [filename.md]
[One to two sentence description of the variant's focus and emphasis.]

## How to use the variants

When reading the variants, pay attention to:

- How each role is described differently across variants. The same position may emphasise different deliverables depending on the target role.
- Technical details that appear in only one or two variants. These are often the most valuable for tailoring.
- Project descriptions and outcomes. Some variants include project narratives that others omit.

After reading all variants, identify the best starting base for the target role and note which specific content from other variants should be pulled in.
```

If "I'll add them later" or "I don't have any yet": write a placeholder `references/cv-variants.md` noting that no variants have been ingested yet. Tell the user they can run `/cv-setup` again to ingest CVs later.

## Step 6: Generate config.yaml

Write `config.yaml` to the project root using all collected values:

```yaml
# CV Tailoring — Personal Configuration
# Generated by /cv-setup. Run /cv-setup again to update.

personal:
  name: ""
  title: ""
  email: ""
  phone: ""
  location: ""
  linkedin: ""
  github: ""
  website: ""
  additional_info: ""  # e.g. "Security Clearance | Full working rights" or "Work authorisation"

writing:
  spelling: ""          # "Australian English", "UK English", or "US English"
  tone: ""              # e.g. "neutral_professional"
  banned_words: []      # list of strings
  team_framing: ""      # e.g. "lead_with_contribution"
  domains: []           # e.g. ["technology", "financial_services"]
  domain_notes: ""      # freeform domain-specific rules

cv:
  target_pages: 3
  sections:
    - summary
    - skills
    - employment
    - certifications
    - education

paths:
  cv_variants: "cv-variants"
  outputs: "outputs"
  jds: "jds"
  skills_log: "skills-log.md"
```

Present a summary and confirm with the user before proceeding.

## Step 7: Generate references/writing-standards.md

Generate `references/writing-standards.md` from scratch using all the configuration collected above. This is the primary writing reference for the cv-tailoring skill — write it as clear, readable prose that Claude can follow directly.

If the user has not configured something explicitly, use intelligent defaults based on their domain context. For example, if they selected Australian Government but did not specify a team framing preference, default to "lead with contribution, note team context where relevant", which is standard for government procurement contexts.

Structure the file as follows. Generate each section based on the user's answers, expanding where needed so the tailoring skill has everything it needs without gaps.

### Tone and language

Write based on:
- The selected spelling convention (apply consistently, give examples for Australian English where helpful: organisation, programme, licence as noun, practise as verb, colour, behaviour)
- The selected tone (neutral/professional, conversational/polished, or formal/traditional)
- The banned words list (include defaults plus any user additions)
- General domain context — government and legal contexts warrant more conservative language even at "neutral" tone

### Accuracy

Write based on:
- The team framing preference
- Domain-specific accuracy expectations

Always include: do not overstate years of experience, seniority, or involvement. Do not claim qualifications not held. Descriptions must reflect what was actually done.

### Domain-specific terminology

Generate one subsection per domain the user selected. Use the knowledge below to write each section. Do not generate sections for domains the user did not select. For anything not explicitly configured by the user, fill in the standard conventions for that domain.

**Technology / software / startups:**
Technical precision matters — name specific technologies, versions, and approaches. Distinguish between "wore many hats" generalism and deep technical ownership. OSS contributions and public technical work are relevant and should be mentioned if present. Quantify scale: users, requests per second, data volume, infrastructure cost. Avoid vague "cloud" references — name the provider and service (AWS Lambda, GCP Cloud Run, Azure AKS).

**Private sector / corporate:**
Commercial language is acceptable but avoid buzzwords. P&L, ARR, cost reduction, and commercial outcome language is appropriate for senior roles. Quantify outcomes where possible (percentage improvements, cost savings, scale of systems). "Stakeholder management" is acceptable but prefer specifics — name the stakeholder level (board, executive, department heads). Avoid passive voice more than in government contexts.

**Financial services and banking:**
Regulatory awareness is valued — APRA, ASIC, AML/CTF obligations are relevant background. Risk language is standard: operational risk, residual risk, control effectiveness. "BAU" (Business as Usual) vs project/change work is a useful distinction. Prefer "financial institution" or the specific entity type (bank, insurer, superannuation fund) over generic "company". Data governance and privacy (CDR, Privacy Act) are increasingly relevant — use precise terminology.

**Consulting and professional services:**
Client-facing experience is central — quantify engagements (number of clients, size, sector). Distinguish between strategy, advisory, implementation, and managed service work. Frameworks (TOGAF, ITIL, PRINCE2, Agile/SAFe) are commonly referenced — note your level of practice, not just awareness. Billable hours and utilisation language is understood but should be used sparingly in CVs.

**Healthcare and medical:**
Use precise clinical terms — do not paraphrase or simplify in ways that change meaning. Regulatory bodies: TGA (Therapeutic Goods Administration), AHPRA (Australian Health Practitioner Regulation Agency). Health data standards: My Health Record, FHIR, HL7 — spell out on first use. Privacy: Health Records Act, Australian Privacy Principles (APPs). "Patient outcomes" and "clinical safety" are high-value phrases in this sector.

**Legal:**
Precision of language is paramount — do not use synonyms for legal terms. Distinguish between advising, appearing, drafting, and negotiating — these are distinct skills. Jurisdiction matters: note whether experience is in federal, state, or territory jurisdiction and the area of law. Formal register throughout. Avoid casual language entirely.

**Engineering and infrastructure:**
Reference relevant Australian Standards (AS/NZS), ISO standards, and professional registrations where held. Engineers Australia membership and CPEng/MIEAust status are significant credentials. Distinguish between design, specification, delivery, and commissioning roles. Quantify: project value, scale, and complexity.

**Academic and research:**
Publications: use standard citation format; distinguish peer-reviewed from other outputs. Grants: name the funding body, amount where appropriate, and your role (CI, co-CI, investigator). Teaching: distinguish undergraduate, postgraduate, supervision, and course coordination. Impact indicators (citations, h-index, research translation) are relevant where measurable.

**Australian Government:**
Security classifications are always PROTECTED, SECRET, TOP SECRET (all caps, no quotes). Key frameworks: ISM (Information Security Manual), PSPF (Protective Security Policy Framework), Essential Eight (capitalised, no hyphen), ASD Blueprint for Secure Cloud. Key agencies: ASD (Australian Signals Directorate), ACSC (Australian Cyber Security Centre), DISP (Defence Industry Security Program). Use "Australian Government" not "Federal Government" or "Commonwealth Government". IRAP (Information Security Registered Assessors Program) — spell out on first use. For accreditation: "IRAP assessment", "accreditation" (not "certification" for systems), "Authority to Operate (ATO)". Essential Eight maturity levels: Maturity Level 0, 1, 2, 3.
**State or Territory Government:**
Use the correct jurisdiction name consistently (e.g. "ACT Government", "Victorian Government" — not "State Government"). Refer to frameworks by their state-specific names. ICT is preferred over IT. If the clearance or security context applies, use the same classification conventions as federal government. Reference the relevant state digital strategy where applicable.

**Defence and intelligence:**
DISP (Defence Industry Security Program) membership is a common requirement — reference precisely. AGSVA (Australian Government Security Vetting Agency) handles personnel security vetting — do not conflate with IRAP. Agencies: ADF (Australian Defence Force), DIO (Defence Intelligence Organisation), DSTG (Defence Science and Technology Group). Clearance levels: Baseline, NV1 (Negative Vetting Level 1), NV2, PV (Positive Vetting) — use these exact terms. Use "capability" not "feature" in Defence contexts. Do not use US military terminology (DoD, ITAR, etc.) unless the role explicitly relates to that context.

### Formatting constraints

Always include these rules regardless of domain:

- Headings must stand alone — no descriptive text on the same line as a heading
- Do not introduce sections with dot-point blurbs — use full paragraphs or full bullet lists, not hybrid formats
- Do not overuse em dashes — prefer commas, parentheses, or sentence restructuring
- No decorative or non-functional formatting (icons, emojis, stylised separators)
- Consistent heading levels and spacing throughout
- No redundant structural elements (repeated summaries, duplicated headings, unnecessary section dividers)
- Never add references to source CV documents unless specifically requested

### CV-specific rules

Write based on the selected sections and target page length. If a page target was given:

- 1–2 pages: flag that concision is critical; roles beyond 7–8 years ago should be summarised or omitted; keep bullet points tight
- 3 pages: standard depth; roles beyond 10 years can be summarised
- 4+ pages: extended role descriptions are appropriate; include more project detail

Always include:
- Profile summaries should read as coherent paragraphs, not lists of claims
- Employment history entries use a short intro paragraph to set context, followed by bullet points for deliverables — do not use narrative paragraphs for the deliverables
- Avoid excessive repetition across roles — vary the framing to show progression
- Skills sections should list capabilities relevant to the target role; remove or deprioritise irrelevant skills
- Do not pad content proportionally

### Supporting document rules

Always include:
- Cover letters: concise (one page), directly address role requirements, do not restate the CV, do not open with "I am writing to apply for..."
- Selection criteria responses: narrative format drawing on specific examples; each response self-contained; typical length three to five paragraphs per criterion
- Pitch documents: clear value proposition for the specific role; avoid generic statements; useful for contract roles or direct engagement

### Custom overrides

Always append this section at the end, empty by default:

```
## Custom overrides

<!-- Add any writing rules specific to your needs below this line. -->
<!-- This section is preserved when /cv-setup is re-run. -->
```

When re-running setup, read the existing `references/writing-standards.md` first and preserve any content that appears below the `<!-- Add any writing rules -->` comment line.

## Step 8: Create initial skills-log.md

If the configured `skills_log` path does not exist, create it:

```markdown
# Skills Log

Running catalogue of experience discovered during CV tailoring sessions that is not yet reflected in the CV variant files. Read this at the start of every session alongside the CV variants.

CV variants remain the source of truth. This log is a fast-access supplement.

## Entry format

Each entry follows this structure:

---
## YYYY-MM-DD | Skill/Experience Area | Short descriptor
- Roles: Role Title @ Org, Role Title @ Org
- Detail: Free-form description of the experience, technically precise.
- Logged during: [Role type] application, [Month Year]
---

## Entries

<!-- New entries are appended below this line during tailoring sessions -->
```

## Completion

Print a summary:

> "Setup complete. You can now use /cv-tailoring to tailor your CV to a job description. Paste a JD or provide a path to a .docx file to get started."
>
> "To update your configuration later, run /cv-setup again."
