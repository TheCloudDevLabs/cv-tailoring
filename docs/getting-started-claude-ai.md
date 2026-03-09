# Getting Started — Claude.ai

This guide covers setting up and using the CV tailoring skill in Claude.ai — the browser-based version of Claude. No installation or technical knowledge is required.

---

## What you'll need

- A **Claude.ai account** — create one free at [claude.ai](https://claude.ai) if you don't have one
- Your **existing CV files** — in Word (.docx), PDF, or plain text format. Multiple versions are ideal but one is enough to get started.
- A **job description** to tailor your CV for (you can add this later)

That's it. No software to install, no terminal, no configuration files.

---

## How the Claude.ai version works

The Claude.ai version uses a two-skill system:

1. **CV Tailoring Setup** — a skill you run once (or whenever your details change). It reads your CV files, asks about your preferences, and generates a personalised **CV Tailoring** skill just for you.

2. **CV Tailoring** — your personalised skill, bundled with your CV variants and writing preferences. This is the skill you use every time you want to tailor a CV.

The setup skill is generic — it works for anyone. The tailoring skill is personalised to you, with your CV content already loaded.

---

## Step 1: Get the setup skill

The setup skill is included in this repository. Build the `.skill` file by running the appropriate command for your operating system from the project directory:

**macOS / Linux:**
```bash
(cd .claude.ai/skills && zip -r ../../cv-tailoring-setup.skill cv-tailoring-setup/)
```

**Windows (PowerShell):**
```powershell
Compress-Archive -Path .claude.ai/skills/cv-tailoring-setup -DestinationPath cv-tailoring-setup.zip
Rename-Item cv-tailoring-setup.zip cv-tailoring-setup.skill
```

Both create `cv-tailoring-setup.skill` in the project root, ready to import.

> If a pre-built release is available on the [Releases page](../../releases), you can download the `.skill` file directly from there instead.

---

## Step 2: Import the setup skill into Claude.ai

1. Go to [claude.ai](https://claude.ai) and sign in
2. Click your profile icon and select **Customizations**
3. Go to the **Skills** tab
4. Click **Add skill** (or drag and drop the `.skill` file)
5. Select the `cv-tailoring-setup.skill` file you built in Step 1

The "CV Tailoring Setup" skill will now appear in your skills list.

---

## Step 3: Run the setup

1. Start a new conversation in Claude.ai
2. Type: **"set up cv tailoring"**

Claude will recognise this and activate the setup skill. You'll see interactive prompts (buttons and options, not just text) guiding you through each step.

### What the setup asks

**Upload your CV files** — Claude will ask you to upload your CV files. Click the attachment button in the chat and select your CV documents. You can upload multiple files — if you have different versions of your CV for different types of roles, upload them all.

**Personal details** — your name, professional title, contact email, phone number, location, LinkedIn profile, GitHub (optional), and personal website (optional). If you have a security clearance, you'll be asked for that too.

**Domain and industry** — which sectors you work in. This is the most important configuration step. For example, if you select "Australian Government", the skill will know to use ISM, PSPF, and Essential Eight terminology correctly. You can select multiple domains if you apply across different sectors.

**Writing preferences** — your preferred spelling (Australian, UK, or US English), tone, and any words or phrases you want Claude to avoid. There's a suggested list of common CV buzzwords you can adopt as defaults.

**CV shape** — your target CV page length and which sections to include.

### What the setup produces

After working through these questions, Claude will:

1. Read and analyse all your uploaded CV files
2. Generate a personalised CV tailoring skill bundled with your data
3. Provide the personalised skill as a downloadable `.skill` file

---

## Step 4: Download and import your personalised skill

When setup finishes, Claude will present a `cv-tailoring.skill` file for download. This file contains:

- The tailoring workflow
- Your CV variants (converted to a format Claude can read efficiently)
- Your personalised writing standards
- Your formatting preferences

**To import it:**

1. Download the `cv-tailoring.skill` file
2. Go back to **Customisations > Skills** in Claude.ai
3. Import the skill the same way you did in Step 2

You now have a "CV Tailoring" skill personalised to you.

---

## Step 5: Tailor your first CV

Start a new conversation in Claude.ai and paste a job description. Say something like:

> "Tailor a CV for this: [paste job description]"

Or just paste the job description — Claude will recognise it and activate the tailoring skill automatically.

### What happens next

**CV review** — Claude reads all your CV variants before doing anything else. It looks at how different roles are described across your variants and identifies the best starting point for this application.

**Gap analysis** — Claude compares the job requirements against your CVs. It tells you clearly what's already well covered, what needs to be repositioned or emphasised differently, and what experience you haven't documented yet.

**Questions** — For each gap, Claude asks you questions one at a time using structured prompts. Typical questions include:
- Do you have experience with [X]?
- At what level — hands-on, oversight, or advisory?
- Which of your roles did this relate to?

You're never asked to write from scratch. You answer questions; Claude does the writing.

**Profile and skills** — Claude proposes a new professional summary and skills section tailored to this role, and confirms with you before moving on.

**Employment history** — Claude works through each role, adjusting the language and emphasis to match what the role requires without overstating your experience.

**Document generation** — Claude produces a formatted Word document you can download.

**Supporting documents** — Claude asks whether you need a cover letter, selection criteria response, or pitch document. If yes, it produces those too.

---

## Getting a cover letter or selection criteria response

If the application requires more than a CV, tell Claude at any point during the session:

> "I also need a cover letter"

or

> "Can you do a selection criteria response for [criterion text]?"

Claude will produce these using the same tailored content and writing standards.

---

## Updating your skill

Your preferences or CV content will change over time. To update:

1. Start a new conversation and say "set up cv tailoring" to run the setup skill again
2. Upload any new CV files along with your existing ones
3. Update any details that have changed
4. Download the newly generated skill file
5. Go to **Customisations > Skills** in Claude.ai, remove the old CV Tailoring skill, and import the new one

You don't need to re-answer everything — the setup skill will ask what you want to update.

---

## Tips for best results

**Upload multiple CV variants.** If you've applied for different types of roles before and have different versions of your CV, upload them all. Claude draws on content from all of them — experience documented in one variant but not another is still available for tailoring.

**Be specific when answering questions.** When Claude asks about a gap in your experience, the more specific your answer the better. "I led the IRAP assessment for the agency's cloud platform in 2023" is more useful than "yes I've done that".

**Tell Claude about the context.** If a job title doesn't capture what the role is really about (e.g. a "Solution Architect" role that's primarily governance-focused), say so when you paste the JD.

**The skill remembers your variants, not your sessions.** Each new conversation starts fresh. Your CV content is bundled in the skill, but the conversation history from previous tailoring sessions is not. This is normal.

---

## Frequently asked questions

**Do I need to pay for Claude.ai?**
The free tier of Claude.ai can run the skill, but it has conversation length limits. For longer sessions (especially with many CV variants or complex role requirements), a paid Claude.ai plan gives you more capacity.

**Are my CV files stored by Anthropic?**
Your CV content is bundled into the `.skill` file that lives on your device. When you use the skill in a conversation, your CV content is sent to Claude as part of that conversation. Anthropic's privacy policy applies to conversation content — see [anthropic.com/privacy](https://anthropic.com/privacy) for details.

**Can I use the skill without uploading all my CV variants?**
Yes. One CV is enough to get started. You can re-run setup later to add more variants.

**The skill isn't triggering when I paste a job description. What do I do?**
Try saying explicitly: "Use the CV tailoring skill to tailor my CV for this role." Or start with "tailor a CV for this:" before pasting the JD.

**Can I edit the generated .docx file?**
Yes. The generated file is a standard Word document. Open it in Microsoft Word, LibreOffice, or Google Docs and edit freely.

---

## Next steps

- Read [how it works](how-it-works.md) to understand what's happening behind the scenes
- If you decide you'd prefer the Claude Code version (with files saved directly to your computer), see [getting started — Claude Code](getting-started-claude-code.md)
