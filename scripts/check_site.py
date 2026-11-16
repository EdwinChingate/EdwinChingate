#!/usr/bin/env python3
"""Check generated project-site links and local assets without extra packages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.links.append(attrs[attr])


def target_file(root, path):
    candidate = root / path.lstrip("/")
    if candidate.is_dir():
        candidate /= "index.html"
    if candidate.suffix == "":
        candidate = candidate / "index.html"
    return candidate


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    baseurl = (sys.argv[2] if len(sys.argv) > 2 else "/EdwinChingate").rstrip("/")
    pages = {p: Links() for p in root.rglob("*.html")}
    errors = []
    if not pages:
        raise SystemExit(f"No generated HTML found in {root}")
    for page, parser in pages.items():
        parser.feed(page.read_text(encoding="utf-8"))
    for page, parser in pages.items():
        for link in parser.links:
            url = urlsplit(link)
            if url.scheme or url.netloc or link.startswith("mailto:"):
                continue
            if url.path.startswith("/"):
                if url.path != baseurl and not url.path.startswith(baseurl + "/"):
                    errors.append(f"{page.relative_to(root)}: root link bypasses baseurl: {link}")
                    continue
                local_path = unquote(url.path[len(baseurl):]) or "/"
            elif url.path:
                local_path = "/" + str((page.parent / unquote(url.path)).relative_to(root))
            else:
                local_path = "/" + str(page.relative_to(root))
            dest = target_file(root, local_path)
            if not dest.is_file():
                errors.append(f"{page.relative_to(root)}: missing target: {link}")
                continue
            if url.fragment and dest.suffix == ".html":
                fragment = unquote(url.fragment)
                if fragment not in pages[dest].ids:
                    errors.append(f"{page.relative_to(root)}: missing fragment: {link}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"Checked internal links in {len(pages)} generated HTML pages.")


if __name__ == "__main__":
    main()
