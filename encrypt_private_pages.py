#!/usr/bin/env python3
"""
Post-build script: encrypts Jekyll pages marked with `private: true` in frontmatter.
Run after `jekyll build`. Requires SITE_PASSWORD environment variable.
Uses staticrypt v3 (installed via npx).
"""
import glob
import os
import shutil
import subprocess
import sys
import tempfile
import yaml

SITE_DIR = "_site"
SKIP_DIRS = {"_site", ".git", "node_modules", "_sass", "_layouts", "_includes", "assets", "bipes"}


def read_frontmatter(path):
    try:
        with open(path, encoding="utf-8") as fh:
            content = fh.read()
        if not content.startswith("---"):
            return None
        parts = content.split("---", 2)
        if len(parts) < 3:
            return None
        return yaml.safe_load(parts[1]) or {}
    except Exception:
        return None


def source_to_output(src):
    """Map a source .md/.html path to its Jekyll _site output path (permalink: pretty)."""
    src = os.path.relpath(src, ".")
    base, _ = os.path.splitext(src)
    if os.path.basename(base) == "index":
        return os.path.join(SITE_DIR, os.path.dirname(base), "index.html")
    return os.path.join(SITE_DIR, base, "index.html")


def find_private_pages():
    results = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            if not f.endswith((".md", ".html")):
                continue
            src = os.path.join(root, f)
            meta = read_frontmatter(src)
            if meta and meta.get("private"):
                results.append((src, source_to_output(src)))
    return results


def encrypt_file(output_path, password):
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            ["npx", "--yes", "staticrypt@3", output_path, "-p", password, "-d", tmpdir],
        )
        if result.returncode != 0:
            print(f"ERROR: staticrypt exited {result.returncode} for {output_path}", file=sys.stderr)
            return False
        # Find the generated file — staticrypt may write just the basename or preserve dirs
        expected = os.path.join(tmpdir, os.path.basename(output_path))
        if os.path.exists(expected):
            encrypted_file = expected
        else:
            matches = glob.glob(os.path.join(tmpdir, "**", "*.html"), recursive=True)
            if not matches:
                print(f"ERROR: staticrypt produced no output for {output_path}", file=sys.stderr)
                return False
            encrypted_file = matches[0]
        shutil.move(encrypted_file, output_path)
    return True


def main():
    password = os.environ.get("SITE_PASSWORD")
    if not password:
        print("ERROR: SITE_PASSWORD environment variable not set", file=sys.stderr)
        sys.exit(1)

    pages = find_private_pages()
    if not pages:
        print("No pages marked private: true — nothing to encrypt.")
        return

    print(f"Found {len(pages)} private page(s) to encrypt.")
    errors = 0
    for src, out in pages:
        if not os.path.exists(out):
            print(f"WARNING: output not found for {src} (expected {out})")
            errors += 1
            continue
        if encrypt_file(out, password):
            print(f"  Encrypted: {out}")
        else:
            errors += 1

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
