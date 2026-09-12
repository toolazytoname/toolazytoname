#!/usr/bin/env python3
"""Refresh the auto-maintained 'Recently shipped' block in README.md.

Uses only the GitHub API + stdlib. Featured bullets above the markers are
left alone; this script only rewrites the block between:

    <!-- recently-shipped:start -->
    <!-- recently-shipped:end -->
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CONFIG = ROOT / ".github" / "profile-maintain.json"
START = "<!-- recently-shipped:start -->"
END = "<!-- recently-shipped:end -->"
REPO_RE = re.compile(r"github\.com/toolazytoname/([A-Za-z0-9._-]+)")
API = "https://api.github.com"


def load_config() -> dict:
    with CONFIG.open(encoding="utf-8") as fh:
        return json.load(fh)


def github_get(url: str, token: str | None) -> tuple[object, dict[str, str]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "toolazytoname-profile-maintain",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return body, {k.lower(): v for k, v in resp.headers.items()}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"GitHub API {exc.code} for {url}: {detail[:400]}") from exc


def next_link(link_header: str | None) -> str | None:
    if not link_header:
        return None
    for part in link_header.split(","):
        if 'rel="next"' in part:
            start = part.find("<") + 1
            end = part.find(">", start)
            if start > 0 and end > start:
                return part[start:end]
    return None


def list_owner_repos(user: str, token: str | None) -> list[dict]:
    url = (
        f"{API}/users/{urllib.parse.quote(user)}/repos"
        f"?per_page=100&type=owner&sort=pushed&direction=desc"
    )
    repos: list[dict] = []
    while url:
        payload, headers = github_get(url, token)
        if not isinstance(payload, list):
            raise SystemExit(f"Unexpected API payload: {type(payload)}")
        repos.extend(payload)
        url = next_link(headers.get("link"))
    return repos


def featured_names(readme: str) -> set[str]:
    before, marker, _ = readme.partition(START)
    if not marker:
        raise SystemExit(f"README.md is missing {START}")
    return {m.group(1) for m in REPO_RE.finditer(before)}


def clip(text: str, limit: int = 140) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def pick_recent(repos: list[dict], *, featured: set[str], cfg: dict) -> list[dict]:
    exclude = {str(name) for name in cfg.get("exclude", [])}
    cutoff = datetime.now(timezone.utc) - timedelta(days=int(cfg["recent_days"]))
    picked: list[dict] = []
    for repo in repos:
        name = repo.get("name") or ""
        pushed = repo.get("pushed_at") or ""
        if not name or name in exclude or name in featured:
            continue
        if repo.get("fork") or repo.get("archived") or repo.get("private"):
            continue
        try:
            when = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        except ValueError:
            continue
        if when < cutoff:
            continue
        picked.append(repo)
        if len(picked) >= int(cfg["max_items"]):
            break
    return picked


def render_block(repos: list[dict], generated_at: datetime) -> str:
    stamp = generated_at.strftime("%Y-%m-%d")
    lines = [
        START,
        f"_Public original repos from the last 90 days that aren't listed above. Last refresh: {stamp}._",
        "",
    ]
    if not repos:
        lines.append("_Featured list is current — nothing extra this week._")
    else:
        for repo in repos:
            name = repo["name"]
            url = repo.get("html_url") or f"https://github.com/toolazytoname/{name}"
            day = (repo.get("pushed_at") or "")[:10]
            desc = clip(repo.get("description") or "")
            if desc:
                lines.append(f"- `{day}` **[{name}]({url})** — {desc}")
            else:
                lines.append(f"- `{day}` **[{name}]({url})**")
    lines.append(END)
    return "\n".join(lines)


def replace_block(readme: str, block: str) -> str:
    start = readme.find(START)
    end = readme.find(END)
    if start < 0 or end < 0 or end < start:
        raise SystemExit("README.md is missing recently-shipped markers")
    end += len(END)
    return readme[:start] + block + readme[end:]


def main() -> int:
    cfg = load_config()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    readme = README.read_text(encoding="utf-8")
    featured = featured_names(readme)
    repos = list_owner_repos(cfg["user"], token)
    recent = pick_recent(repos, featured=featured, cfg=cfg)
    now = datetime.now(timezone.utc)
    updated = replace_block(readme, render_block(recent, now))
    if updated == readme:
        print("README already up to date")
        return 0
    README.write_text(updated, encoding="utf-8")
    print(f"Updated recently-shipped: {len(recent)} repos")
    for repo in recent:
        print(f"  - {repo['name']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
