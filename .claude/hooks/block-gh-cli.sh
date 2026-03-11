#!/bin/bash
# Block gh CLI usage — all GitHub operations must use ~/.claude/scripts/gh-app.py
COMMAND=$(jq -r '.tool_input.command')

if echo "$COMMAND" | grep -qE '\bgh\s+(issue|pr|api|auth)\b'; then
  jq -n '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: "BLOCKED: Use ~/.claude/scripts/gh-app.py instead of gh CLI. See CLAUDE.md for usage."
    }
  }'
else
  exit 0
fi
