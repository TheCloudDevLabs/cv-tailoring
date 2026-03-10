#!/usr/bin/env python3
"""Analyse recent changes to skill files and code, then update docs accordingly.

Called by the docs-update GitHub Actions workflow. Reads the git diff for
watched paths, sends it to Claude along with current doc content, and writes
back any suggested updates.

Signals outcome via GITHUB_OUTPUT:
    docs_changed=true   — at least one doc file was updated
    docs_changed=false  — no changes needed
"""

import os
import re
import subprocess
import sys
from pathlib import Path

import anthropic

WATCHED_PATHS = [".claude/skills/", "generate_cv.py", "config.example.yaml"]

DOC_FILES = [
    "README.md",
    "docs/getting-started-claude-code.md",
    "docs/getting-started-claude-ai.md",
    "docs/how-it-works.md",
]


def get_diff() -> str:
    result = subprocess.run(
        ["git", "diff", "HEAD~1", "HEAD", "--"] + WATCHED_PATHS,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def read_docs() -> dict:
    docs = {}
    for path in DOC_FILES:
        p = Path(path)
        if p.exists():
            docs[path] = p.read_text(encoding="utf-8")
    return docs


def call_claude(diff: str, docs: dict) -> str:
    client = anthropic.Anthropic()

    docs_xml = "\n\n".join(
        f'<file path="{path}">\n{content}\n</file>'
        for path, content in docs.items()
    )

    prompt = f"""You are a documentation maintainer for the cv-tailoring project — \
a Claude skill that tailors CVs to job descriptions.

Here are recent changes to skill files and/or code:

<diff>
{diff}
</diff>

Here are the current documentation files:

{docs_xml}

Analyse the diff and determine if any documentation needs updating to accurately \
reflect the changes.

Rules:
- Only update docs when the changes are substantive and user-facing (new features, \
changed behaviour, renamed commands, new requirements, etc.)
- Do not make cosmetic or stylistic changes
- Do not add content not evidenced by the diff
- Preserve the existing tone, structure, and formatting of each document
- If changes only affect internal implementation details, no update is needed

If no documentation updates are needed, respond with exactly:
NO_UPDATES_NEEDED

Otherwise, for each file that needs updating, provide the COMPLETE updated file \
content using this format — include only files that actually need changes:

<file path="README.md">
[complete updated content]
</file>"""

    with client.messages.stream(
        model="claude-opus-4-6",
        max_tokens=32000,
        thinking={"type": "adaptive"},
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        final = stream.get_final_message()

    return "".join(
        block.text for block in final.content if block.type == "text"
    )


def parse_updates(response: str, known_paths: set) -> dict:
    if "NO_UPDATES_NEEDED" in response:
        return {}

    updates = {}
    pattern = r'<file path="([^"]+)">(.*?)</file>'
    for path, content in re.findall(pattern, response, re.DOTALL):
        if path in known_paths:
            updates[path] = content.strip()
    return updates


def set_github_output(key: str, value: str) -> None:
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"{key}={value}\n")
    else:
        print(f"GITHUB_OUTPUT not set — would write: {key}={value}")


def main() -> None:
    diff = get_diff()
    if not diff.strip():
        print("No relevant changes detected.")
        set_github_output("docs_changed", "false")
        return

    print(f"Diff detected ({len(diff)} chars). Calling Claude to review docs...")

    docs = read_docs()
    response = call_claude(diff, docs)
    updates = parse_updates(response, set(docs.keys()))

    if not updates:
        print("No documentation updates needed.")
        set_github_output("docs_changed", "false")
        return

    for path, content in updates.items():
        Path(path).write_text(content, encoding="utf-8")
        print(f"Updated: {path}")

    set_github_output("docs_changed", "true")
    print(f"\n{len(updates)} file(s) updated.")


if __name__ == "__main__":
    main()
