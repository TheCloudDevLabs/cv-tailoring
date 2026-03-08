# Document Template

This reference defines the formatting specification for CV and supporting documents.

## CV layout

The CV uses a single-column layout with no tables. All content flows top to bottom. The formatting is handled by the centralised `generate_cv.py` module — Claude builds a content dict and calls the function. See SKILL.md Step 6 for the schema and invocation instructions.

### Page properties

- Page size: A4 (8.27" x 11.69")
- Margins: top 0.76", bottom 0.69", left 0.83", right 0.83"
- Font: Calibri throughout
- Base font size: 10pt for body text
- Text colour: #2E3440 (dark grey)

### Header section

- Name: Calibri 18pt bold, 2pt space after
- Title: Calibri 12pt regular, 1pt space after
- Contact line: Calibri 9.5pt, pipe-separated (email | phone | location), 1pt space after
- LinkedIn + additional info line: LinkedIn as hyperlink at 9.5pt, pipe separator, additional info (e.g. clearance, work rights) bold at 9.5pt, 5pt space after

### Section headings

"Professional Summary", "Core Skills", "Experience", "Certifications", "Courses"

- Calibri 11pt bold
- 15pt space before, 5pt space after

### Professional Summary

Two to four paragraphs covering career overview, domain focus, and key capabilities relevant to the target role. Body font size, 4pt before/after each paragraph.

### Core Skills

A single line of skill labels separated by middots (·). Calibri 9.5pt, 4pt before/after.

### Employment History

Each role formatted as:

1. **Role title:** Calibri 10.5pt bold, 12pt space before
2. **Organisation | dates:** Organisation in italic, dates in regular weight, pipe-separated. 1pt before, 1pt after
3. **Brief intro paragraph** (optional): One to two sentences of context for the role. Body font size, 4pt before/after. Only include when the role needs context-setting.
4. **Bullet points:** Specific deliverables and outcomes as bullet points. List Paragraph style, 2pt before/after each bullet.

**Important:** Employment history must always use the brief-intro-plus-bullets format. Do not use narrative paragraphs for deliverables.

### Certifications

Dash-prefixed list items, body font size, 2pt space after each.

### Courses

Dash-prefixed list items, body font size, 2pt space after each. This section is optional.

### Footer

"References available upon request." in italic, 12pt space before.

## Supporting document layout

Cover letters, selection criteria responses, and pitch documents use a simpler single-column layout.

### Page properties

- Page size: A4
- Margins: top 1440 DXA (1 inch), bottom 1440 DXA, left 1440 DXA, right 1440 DXA
- Font: Calibri throughout
- Base font size: 11pt for body text

### Header

- Name: bold, 14pt
- Contact line: regular, 10pt (email, phone, location on one line, separated by pipes or similar)
- Additional info line (e.g. clearance, work authorisation): bold, 10pt (if applicable)

### Body

- Section headings (for selection criteria): bold, 11pt
- Body text: 11pt, paragraph format
- No bullet lists unless specifically appropriate for the content
- Single spacing with 120 DXA between paragraphs

### Cover letter specifics

- Date at top
- Addressee if known (otherwise "Dear Hiring Manager" or equivalent)
- Three to four paragraphs maximum
- Sign-off with name

### Selection criteria specifics

- Each criterion as a separate section with the criterion text as a heading
- Narrative response using specific project examples from the CV
- Each response should be self-contained (assume the reader may jump between criteria)
- Typical length: three to five paragraphs per criterion
