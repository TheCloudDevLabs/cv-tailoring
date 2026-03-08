CV Tailoring Process

This document defines the process for tailoring {{USER_NAME}}'s CV to specific job
applications. Follow the steps in order for each new application. All questions
during the process are presented using interactive widget prompts.

What You Provide

Paste the job description into the chat. If the role has a specific emphasis that
is not obvious from the title (for example, a Solution Architect role that is
primarily governance-focused), flag that alongside the job description.

Process Steps

1.  **Full CV review.** Read every CV variant in the skill files before doing
    anything else. Each variant contains different technical details, project
    descriptions, and role emphases that may not appear in others. The full
    set of variants is:

{{VARIANT_LIST}}

    Do not rely on a single base CV. Experience relevant to the target role
    may only be documented in one or two of these variants. After reviewing
    all files, identify which variant is the best starting base, and note any
    additional content from other variants that should be incorporated.

2.  **Gap analysis.** Compare the job requirements against the content found
    across all CV variants. Identify what is well covered, what needs
    repositioning, and any areas where experience is not yet documented in any
    variant. Present the gap analysis clearly, distinguishing between content
    that already exists and needs tailoring versus genuinely undocumented
    experience that requires input.

3.  **Question-driven alignment.** For each gap or underdocumented area,
    work through it using a structured question sequence. Address one gap at
    a time using the following approach:

    a.  **Initial question.** Use a widget prompt to ask whether the user has
        relevant experience in the gap area.

    b.  **Level of experience.** Once confirmed, follow up to establish depth.
        Distinguish between hands-on delivery, technical oversight, advisory
        input, or strategic direction.

    c.  **Role attribution.** Ask which roles or engagements the experience
        was part of. List relevant roles as multi-select options.

    d.  **Clarification if needed.** Optional final question if framing is
        still ambiguous after the previous prompts.

    Move to the next gap only after the current one is fully resolved.

    Note: In the Claude Code version of this skill, a persistent skills log
    records undocumented experience discovered during previous tailoring
    sessions. That log is not available in Claude.ai — each conversation
    starts fresh with only the CV variants bundled in the skill.

4.  **Profile and skills review.** Propose profile and skills section changes
    first. Confirm direction before moving to employment history.

5.  **Employment history.** Work through each role systematically, adjusting
    language and emphasis to match the target without overstating experience.
    Draw on content from all CV variants where relevant.

6.  **Document generation.** Produce the final CV as a downloadable .docx
    file presented as an attachment in the conversation.

    Note: In the Claude Code version, the tailored CV is also saved back to
    the cv-variants directory as a Markdown file for use in future sessions.
    In Claude.ai, the CV content exists only within this conversation — if
    you want to preserve it for future use, download the generated .docx and
    re-upload it when running setup again to add it as a new variant.

7.  **Supporting documents.** Once the CV is complete, use a widget prompt to
    ask whether additional documents are needed: cover letter, pitch document,
    selection criteria response, or none. If requested, produce each as a
    separate .docx file using the same writing standards.

Widget Prompt Guidelines

All questions should be presented using the interactive widget prompt tool. The
following principles apply:

-   Present one gap area at a time.
-   Ask initial question, level, and role attribution as separate sequential prompts.
-   Use short, clear option labels.
-   Prefer multi-select where more than one option may apply.
-   Use ranking prompts when order of emphasis matters.
-   Only use freeform prompts for genuinely open-ended inputs.
-   Always include a brief conversational message before presenting the widget.

Decisions That Require Your Input

-   Whether a requirement can be legitimately claimed based on actual experience
-   How to frame experience that partially matches a requirement
-   Any role-specific context, such as knowledge of the hiring organisation or team

To Start a New Application

Paste the job description and say "tailor a CV for this." The process above
will run from step one.
