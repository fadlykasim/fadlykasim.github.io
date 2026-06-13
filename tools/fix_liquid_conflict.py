#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wrap a post's body in Liquid raw tags to escape `{{` / `{%` conflicts.

Copyright (c) 2026 Fadly Kasim <fadly.kasim@gmail.com>
All rights reserved.

Licensed under the MIT License.

Usage:
    python tools/fix_liquid_conflict.py _posts/2008-03-20-foo.md [more.md ...]
"""

import sys


RAW_OPEN = "{% raw %}"
RAW_CLOSE = "{% endraw %}"


def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    parts = content.split("---", 2)
    if len(parts) != 3:
        print(f"  ✗ Front matter not found: {filepath}")
        return False

    body = parts[2].strip()
    if RAW_OPEN in body:
        print(f"  · Already wrapped: {filepath}")
        return False

    wrapped = f"---{parts[1]}---\n\n{RAW_OPEN}\n{body}\n{RAW_CLOSE}\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(wrapped)
    print(f"  ✓ Wrapped: {filepath}")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/fix_liquid_conflict.py <file1> [file2 ...]")
        sys.exit(1)

    for path in sys.argv[1:]:
        fix_file(path)


if __name__ == "__main__":
    main()
