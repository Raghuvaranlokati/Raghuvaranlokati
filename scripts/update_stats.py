#!/usr/bin/env python3
"""
Automated GitHub Stats & Streak Updater
Fetches real-time GitHub streaks and contribution counts, then updates
assets/github-streak.svg and assets/github-stats.svg.
"""

import os
import re
import sys
import json
import urllib.request

USERNAME = os.environ.get("GITHUB_USERNAME", "Raghuvaranlokati")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STREAK_SVG_PATH = os.path.join(BASE_DIR, "assets", "github-streak.svg")
STATS_SVG_PATH = os.path.join(BASE_DIR, "assets", "github-stats.svg")


def fetch_streak_data(username):
    url = f"https://streak-stats.demolab.com/?user={username}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        content = resp.read().decode("utf-8")

    items = []
    for m in re.finditer(r"<text[^>]*>\s*([^\s<][^<]*?)\s*</text>", content):
        items.append(m.group(1).strip())

    total_contributions = None
    current_streak = None
    longest_streak = None

    for i, item in enumerate(items):
        if item == "Total Contributions" and i > 0:
            total_contributions = items[i - 1]
        elif item == "Current Streak":
            for j in range(i + 1, len(items)):
                val = items[j].replace(",", "")
                if val.isdigit():
                    current_streak = items[j]
                    break
        elif item == "Longest Streak" and i > 0:
            longest_streak = items[i - 1]

    if not current_streak or not longest_streak or not total_contributions:
        raise ValueError(f"Failed to parse streak data. Extracted items: {items}")

    return {
        "total_contributions": total_contributions,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
    }


def fetch_user_meta(username):
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {
                "public_repos": data.get("public_repos"),
            }
    except Exception as e:
        print(f"Warning: Could not fetch user metadata from GitHub API: {e}", file=sys.stderr)
        return {}


def update_streak_svg(data):
    if not os.path.exists(STREAK_SVG_PATH):
        print(f"Error: {STREAK_SVG_PATH} not found", file=sys.stderr)
        return False

    with open(STREAK_SVG_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Total Contributions: replace number above Total Contributions
    content = re.sub(
        r'(<text[^>]*class="mono">)[^<]+(\+</text>\s*<text[^>]*>Total Contributions</text>)',
        rf'\g<1>{data["total_contributions"]}\g<2>',
        content
    )

    # 2. Current Streak: replace number above Current Streak
    content = re.sub(
        r'(<text[^>]*class="mono">)[^<]+Days(</text>\s*<text[^>]*>Current Streak</text>)',
        rf'\g<1>{data["current_streak"]} Days\g<2>',
        content
    )

    # 3. Highest Streak: replace number above Highest Streak
    content = re.sub(
        r'(<text[^>]*class="mono">)[^<]+Days(</text>\s*<text[^>]*>Highest Streak</text>)',
        rf'\g<1>{data["longest_streak"]} Days\g<2>',
        content
    )

    if content != original:
        with open(STREAK_SVG_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {STREAK_SVG_PATH}: Current={data['current_streak']} Days, Longest={data['longest_streak']} Days, Total={data['total_contributions']}+")
        return True
    else:
        print(f"No changes required for {STREAK_SVG_PATH}.")
        return False


def update_stats_svg(streak_data, user_meta):
    if not os.path.exists(STATS_SVG_PATH):
        return False

    with open(STATS_SVG_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Update Total Contributions in stats.svg
    content = re.sub(
        r'(<text[^>]*>Total Contributions:</text>\s*<text[^>]*class="mono">)[^<]+(</text>)',
        rf'\g<1>{streak_data["total_contributions"]}+\g<2>',
        content
    )

    # Update Public Repositories in stats.svg if fetched
    if user_meta.get("public_repos") is not None:
        content = re.sub(
            r'(<text[^>]*>Public Repositories:</text>\s*<text[^>]*class="mono">)[^<]+(</text>)',
            rf'\g<1>{user_meta["public_repos"]}\g<2>',
            content
        )

    if content != original:
        with open(STATS_SVG_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {STATS_SVG_PATH}.")
        return True
    else:
        print(f"No changes required for {STATS_SVG_PATH}.")
        return False


def main():
    print(f"Fetching streak data for {USERNAME}...")
    try:
        streak_data = fetch_streak_data(USERNAME)
        print(f"Fetched live streak data: {streak_data}")
    except Exception as e:
        print(f"Error fetching streak data: {e}", file=sys.stderr)
        sys.exit(1)

    user_meta = fetch_user_meta(USERNAME)

    changed_streak = update_streak_svg(streak_data)
    changed_stats = update_stats_svg(streak_data, user_meta)

    if changed_streak or changed_stats:
        print("Successfully updated SVG statistics!")
    else:
        print("All SVGs are already up to date.")


if __name__ == "__main__":
    main()
