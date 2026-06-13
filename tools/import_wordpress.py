#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Import all posts from a WordPress.com blog into Jekyll _posts/ directory.

Copyright (c) 2026 Fadly Kasim <fadly.kasim@gmail.com>
All rights reserved.

Licensed under the MIT License.

Usage:
    python tools/import_wordpress.py
"""

import os
import re
import sys
import time
import requests
import html2text
from datetime import datetime

# ----- Konfigurasi -----
WP_SITE = "firstly.wordpress.com"
OUTPUT_DIR = "_posts"
CATEGORY = "archive"
# -----------------------

API_URL = f"https://public-api.wordpress.com/wp/v2/sites/{WP_SITE}/posts"


def slugify(text):
    """Convert text to safe filename slug."""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text[:80] or 'post'


def yaml_escape(text):
    """Escape string for safe inclusion in YAML front matter."""
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('"', '\\"').strip()
    return text


def fetch_all_posts():
    """Fetch all posts with pagination."""
    posts = []
    page = 1
    while True:
        print(f"Fetching page {page}...", end=' ', flush=True)
        try:
            resp = requests.get(API_URL, params={
                "per_page": 100,
                "page": page,
                "_fields": "id,date,slug,title,content,categories,tags,link"
            }, timeout=30)
        except requests.RequestException as e:
            print(f"\nERROR: {e}")
            break

        if resp.status_code in (400, 404):
            print("(no more pages)")
            break
        if resp.status_code != 200:
            print(f"\nUnexpected status: {resp.status_code}")
            print(resp.text[:500])
            break

        batch = resp.json()
        if not batch:
            print("(empty)")
            break

        posts.extend(batch)
        print(f"got {len(batch)} posts (total so far: {len(posts)})")
        page += 1
        time.sleep(0.5)

    return posts


def html_to_markdown(html):
    """Convert HTML to clean Markdown."""
    h = html2text.HTML2Text()
    h.body_width = 0
    h.unicode_snob = True
    h.ignore_emphasis = False
    h.ignore_links = False
    h.ignore_images = False
    return h.handle(html).strip()


def save_post(post):
    """Convert a WP post to Jekyll markdown and save."""
    date_str = post['date'][:10]
    full_date = post['date']
    title = post['title']['rendered']
    content_html = post['content']['rendered']
    slug = post.get('slug') or slugify(title)
    original_url = post.get('link', '')

    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    content_md = html_to_markdown(content_html)

    front_matter = f"""---
layout: post
title: "{yaml_escape(title)}"
date: {full_date}+0800
categories: [{CATEGORY}]
tags: [wordpress, imported]
original_url: {original_url}
---

> Tulisan ini di-import dari [blog WordPress saya yang lama]({original_url}), \
ditulis pada {date_str}.

{content_md}
"""

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(front_matter)

    return filepath


def main():
    print(f"Fetching all posts from {WP_SITE}...")
    posts = fetch_all_posts()

    if not posts:
        print("No posts found. Exiting.")
        sys.exit(1)

    print(f"\nTotal posts fetched: {len(posts)}")
    print(f"Date range: {posts[-1]['date'][:10]} → {posts[0]['date'][:10]}\n")

    saved = 0
    for post in posts:
        try:
            path = save_post(post)
            print(f"  ✓ {path}")
            saved += 1
        except Exception as e:
            print(f"  ✗ Error on post {post.get('id')}: {e}")

    print(f"\nDone! Imported {saved}/{len(posts)} posts to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
