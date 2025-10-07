#!/usr/bin/env python3
import re
import sys

# Your commit regex
pattern = (
    r"^\[#\d] (feat|fix|docs|style|refactor|test|chore|perf) - .+"
    r"|^\[fix\] - .+"
)

commit_msg_file = sys.argv[1]
with open(commit_msg_file) as f:
    first_line = f.readline().strip()

if not re.match(pattern, first_line):
    print("❌ ERROR: Commit message does not follow the required format:")
    print("[type-NT<ticket_number>-team] - Short description")
    print(f"Your message was: {first_line}")
    sys.exit(1)

sys.exit(0)