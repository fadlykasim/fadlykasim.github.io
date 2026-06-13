#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch the Chirpy pages-deploy.yml to relax htmlproofer for legacy imported posts.

Copyright (c) 2026 Fadly Kasim <fadly.kasim@gmail.com>
All rights reserved.

Licensed under the MIT License.
"""

import re
import sys

WORKFLOW = ".github/workflows/pages-deploy.yml"

with open(WORKFLOW) as f:
    content = f.read()

# Find the htmlproofer command and replace it
new_htmlproofer = '''bundle exec htmlproofer _site \\
            --disable-external=true \\
            --enforce-https=false \\
            --allow-hash-href \\
            --allow-missing-href \\
            --ignore-status-codes "0,404,503" \\
            --ignore-urls "/^http:\\/\\/127.0.0.1/,/^http:\\/\\/0.0.0.0/,/^http:\\/\\/localhost/,/^http:\\/\\/$/"'''

# Replace the existing htmlproofer line (whole block)
pattern = r'bundle exec htmlproofer.*?(?=\n\s*(?:-|$))'
content = re.sub(pattern, new_htmlproofer, content, count=1, flags=re.DOTALL)

with open(WORKFLOW, 'w') as f:
    f.write(content)

print(f"Patched: {WORKFLOW}")
print("\nPlease review the changes with:")
print(f"  cat {WORKFLOW}")
