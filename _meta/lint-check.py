#!/usr/bin/env python3
"""Wiki lint v2 - 12 health checks, with false-positive suppression"""

import os
import re
from collections import defaultdict
from datetime import date

WIKI = "/root/wiki"
today = date.today()

# Templates/text files that legitimately reference [[X]] as syntax examples
TEMPLATE_FILES = {'SCHEMA.md', 'README.md', 'index.md', 'log.md'}

# Pages with stub status (low confidence expected)
STUB_PAGES = set()

# ============ 0. Page inventory ============
all_pages = []
for root, dirs, files in os.walk(WIKI):
    if any(skip in root for skip in ['/raw/', '/_meta/', '/.git', '/archive']):
        continue
    for f in files:
        if f.endswith('.md') and not f.startswith('_'):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, WIKI)
            all_pages.append(rel)

print(f"=== Wiki Lint Report (v2) ===")
print(f"Date: {today}")
print(f"Total content pages: {len(all_pages)}")
print()

# ============ Build wikilink map ============
wikilink_pattern = re.compile(r'\[\[([^\]]+)\]\]')
inbound = defaultdict(list)
outbound = defaultdict(list)

for page in all_pages:
    full = os.path.join(WIKI, page)
    with open(full, 'r', encoding='utf-8') as f:
        content = f.read()
    links = wikilink_pattern.findall(content)
    for link in links:
        link_clean = link.split('|')[0].strip()
        inbound[link_clean].append(page)
        outbound[page].append(link_clean)

# Build set of page slugs
page_slugs = set()
for page in all_pages:
    base = os.path.basename(page).replace('.md', '')
    page_slugs.add(base)

# ============ ① Orphan pages ============
print("=" * 60)
print("① Orphan Pages (no inbound wikilinks)")
print("=" * 60)
orphans = []
for page in all_pages:
    base = os.path.basename(page).replace('.md', '')
    if base in ('index', 'log', 'SCHEMA', 'README'):
        continue
    if base not in inbound or len(inbound[base]) == 0:
        orphans.append(page)

if orphans:
    for o in orphans:
        print(f"  ❌ {o}")
else:
    print("  ✅ No orphans")

# ============ ② Broken wikilinks (template-aware) ============
print()
print("=" * 60)
print("② Broken Wikilinks (excluding template text)")
print("=" * 60)
broken = []
TEMPLATE_LINKS = {'page-slug', 'wikilinks', 'page-name', 'page-title', 'entity-name'}
for src, links in outbound.items():
    # Skip template text in index.md/SCHEMA.md/README.md
    if os.path.basename(src) in TEMPLATE_FILES:
        continue
    for link in links:
        if link in TEMPLATE_LINKS:
            continue
        if link not in page_slugs:
            broken.append((src, link))

if broken:
    for src, link in broken:
        print(f"  ❌ {src} -> [[{link}]]")
else:
    print("  ✅ All wikilinks resolve")

# ============ ③ Index completeness ============
print()
print("=" * 60)
print("③ Index.md Completeness")
print("=" * 60)
with open(os.path.join(WIKI, 'index.md'), 'r') as f:
    index_content = f.read()
indexed_links = set(wikilink_pattern.findall(index_content))
indexed_slugs = set(l.split('|')[0].strip() for l in indexed_links)

missing_from_index = []
for page in all_pages:
    base = os.path.basename(page).replace('.md', '')
    if base in ('index', 'log', 'SCHEMA', 'README'):
        continue
    if base not in indexed_slugs:
        missing_from_index.append(base)

if missing_from_index:
    for m in missing_from_index:
        print(f"  ❌ Not in index: {m}")
else:
    print(f"  ✅ All {len(all_pages)} pages indexed")

# ============ ④ Frontmatter validation ============
print()
print("=" * 60)
print("④ Frontmatter Validation")
print("=" * 60)
fm_required = ['title:', 'created:', 'updated:', 'type:', 'agent:', 'visibility:', 'tags:']
fm_issues = []
for page in all_pages:
    if any(skip in page for skip in ['SCHEMA.md', 'README.md', 'index.md', 'log.md']):
        continue
    full = os.path.join(WIKI, page)
    with open(full) as f:
        content = f.read()
    if not content.startswith('---'):
        fm_issues.append((page, "missing frontmatter"))
        continue
    fm_end = content.find('---', 3)
    if fm_end == -1:
        fm_issues.append((page, "unterminated frontmatter"))
        continue
    fm = content[3:fm_end]
    for req in fm_required:
        if req not in fm:
            fm_issues.append((page, f"missing {req}"))

if fm_issues:
    for p, issue in fm_issues:
        print(f"  ❌ {p}: {issue}")
else:
    print(f"  ✅ All pages have complete frontmatter")

# ============ ⑤ Stale content ============
print()
print("=" * 60)
print("⑤ Stale Content (updated >90 days old)")
print("=" * 60)
stale = []
for page in all_pages:
    if any(skip in page for skip in ['SCHEMA.md', 'README.md', 'index.md', 'log.md']):
        continue
    full = os.path.join(WIKI, page)
    with open(full) as f:
        content = f.read()
    m = re.search(r'^updated:\s*(\d{4}-\d{2}-\d{2})', content, re.M)
    if m:
        d = date.fromisoformat(m.group(1))
        days = (today - d).days
        if days > 90:
            stale.append((page, days))

if stale:
    for p, days in stale:
        print(f"  ⚠️  {p}: {days} days old")
else:
    print("  ✅ No stale pages (all <90 days)")

# ============ ⑥ Contradictions (excluding schema example) ============
print()
print("=" * 60)
print("⑥ Contradictions")
print("=" * 60)
contradictions = []
for page in all_pages:
    full = os.path.join(WIKI, page)
    with open(full) as f:
        content = f.read()
    # Skip SCHEMA.md (it's a template/spec, contains example values)
    if 'SCHEMA.md' in page:
        continue
    if 'contested: true' in content or 'contradictions:' in content:
        contradictions.append((page, "contested: true" if 'contested: true' in content else "contradictions field"))

if contradictions:
    for p, reason in contradictions:
        print(f"  ⚠️  {p}: {reason}")
else:
    print("  ✅ No contested pages")

# ============ ⑦ Low confidence ============
print()
print("=" * 60)
print("⑦ Low Confidence Pages (excluding stubs)")
print("=" * 60)
low_conf = []
for page in all_pages:
    if any(skip in page for skip in ['SCHEMA.md', 'README.md', 'index.md', 'log.md']):
        continue
    full = os.path.join(WIKI, page)
    with open(full) as f:
        content = f.read()
    # Skip stubs
    if 'status: stub' in content:
        continue
    m = re.search(r'confidence:\s*(\w+)', content)
    if m and m.group(1) in ('low',):
        low_conf.append((page, m.group(1)))

if low_conf:
    for p, c in low_conf:
        print(f"  ⚠️  {p}: confidence={c}")
else:
    print("  ✅ No low confidence pages")

# ============ ⑧ Source drift ============
print()
print("=" * 60)
print("⑧ Source Drift (raw/)")
print("=" * 60)
print("  ⏭️  Skipped (raw/ files mirrored, no sha256 tracking)")

# ============ ⑨ Page size ============
print()
print("=" * 60)
print("⑨ Page Size (over 200 lines, excluding index/README/log)")
print("=" * 60)
oversize = []
for page in all_pages:
    # Exclude docs that are allowed to be long
    if any(skip in page for skip in ['SCHEMA.md', 'README.md', 'index.md', 'log.md']):
        continue
    full = os.path.join(WIKI, page)
    with open(full) as f:
        lines = f.readlines()
    if len(lines) > 200:
        oversize.append((page, len(lines)))

if oversize:
    for p, n in oversize:
        print(f"  ⚠️  {p}: {n} lines")
else:
    print(f"  ✅ All content pages ≤200 lines")

# ============ ⑩ Tag audit ============
print()
print("=" * 60)
print("⑩ Tag Audit")
print("=" * 60)
with open(os.path.join(WIKI, 'SCHEMA.md')) as f:
    schema = f.read()

m = re.search(r'## Tag Taxonomy\n(.*?)## ', schema, re.S)
if m:
    taxonomy_section = m.group(1)
    schema_tag_list = re.findall(r'`([\w-]+)`', taxonomy_section)
    schema_set = set(schema_tag_list)
else:
    schema_set = set()

all_used_tags = defaultdict(int)
for page in all_pages:
    full = os.path.join(WIKI, page)
    with open(full) as f:
        content = f.read()
    m = re.search(r'^tags:\s*\[(.*?)\]', content, re.M)
    if m:
        tags = re.findall(r'\b([\w-]+)\b', m.group(1))
        for t in tags:
            all_used_tags[t] += 1

print(f"  Total used tags: {len(all_used_tags)}")
unknown_tags = []
for tag, count in sorted(all_used_tags.items()):
    if schema_set and tag not in schema_set:
        unknown_tags.append((tag, count))

if unknown_tags:
    for t, c in unknown_tags:
        print(f"  ⚠️  `{t}` used {c}x but not in SCHEMA taxonomy")
else:
    print(f"  ✅ All tags in taxonomy")

# ============ ⑪ Log rotation ============
print()
print("=" * 60)
print("⑪ Log Size")
print("=" * 60)
log_file = os.path.join(WIKI, 'log.md')
with open(log_file) as f:
    log_content = f.read()
log_entries = log_content.count('### [') + log_content.count('## [')
print(f"  Total entries: {log_entries} (threshold: 500)")
if log_entries > 500:
    print(f"  ⚠️  ROTATION NEEDED")
else:
    print(f"  ✅ OK")

# ============ ⑫ Summary ============
print()
print("=" * 60)
print("⑫ Summary")
print("=" * 60)
print(f"  Pages: {len(all_pages)}")
print(f"  Wikilinks: {sum(len(v) for v in outbound.values())}")
print(f"  Orphans: {len(orphans)}")
print(f"  Broken links (real): {len(broken)}")
print(f"  Missing from index: {len(missing_from_index)}")
print(f"  Frontmatter issues: {len(fm_issues)}")
print(f"  Stale (>90d): {len(stale)}")
print(f"  Contradictions: {len(contradictions)}")
print(f"  Low confidence (excluding stubs): {len(low_conf)}")
print(f"  Oversize content pages: {len(oversize)}")
print(f"  Unknown tags: {len(unknown_tags)}")

# Score
total_checks = 9  # 1-9 with content
issues = len(orphans) + len(broken) + len(missing_from_index) + len(fm_issues) + len(stale) + len(contradictions) + len(low_conf) + len(oversize) + len(unknown_tags)
if issues == 0:
    print(f"\n  🎉 ALL CHECKS PASSED! Wiki is healthy.")
else:
    print(f"\n  ⚠️  {issues} issues to fix")
