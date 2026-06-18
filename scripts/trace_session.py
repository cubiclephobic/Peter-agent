#!/usr/bin/env python3
"""Print one line per step (timestamp, action type, tool name, token count) from a session JSONL file."""
import json
import sys


def describe(entry):
    timestamp = entry.get("timestamp", "")
    msg = entry.get("message", {})
    content = msg.get("content")

    action = entry.get("type", "unknown")
    tool_name = ""
    tokens = ""

    if isinstance(content, list):
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                action = "tool_use"
                tool_name = block.get("name", "")
            elif block.get("type") == "tool_result":
                action = "tool_result"

    usage = msg.get("usage")
    if isinstance(usage, dict):
        total = usage.get("input_tokens", 0) + usage.get("output_tokens", 0)
        if total:
            tokens = str(total)

    return timestamp, action, tool_name, tokens


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <session.jsonl>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            timestamp, action, tool_name, tokens = describe(entry)
            print(f"{timestamp}\t{action}\t{tool_name}\t{tokens}")


if __name__ == "__main__":
    main()
