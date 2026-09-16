from collections import Counter
from typing import Iterable, Mapping


def _hours(row: Mapping[str, str]) -> float:
    value = (row.get("hours_played") or "").strip()
    if not value:
        return 0.0
    try:
        hours = float(value)
    except ValueError as error:
        raise ValueError(f"invalid hours_played: {value!r}") from error
    if hours < 0:
        raise ValueError("hours_played cannot be negative")
    return hours


def markdown_report(rows: Iterable[Mapping[str, str]]) -> str:
    games = []
    platforms = Counter()
    total_hours = 0.0
    for row in rows:
        title = (row.get("title") or "").strip()
        if not title:
            raise ValueError("each row must have a title")
        platform = (row.get("platform") or "Unknown").strip() or "Unknown"
        games.append((title, platform, _hours(row)))
        platforms[platform] += 1
        total_hours += games[-1][2]

    lines = [
        "# Game Library Report",
        "",
        f"- **Games:** {len(games)}",
        f"- **Hours played:** {total_hours:.1f}",
        "",
        "## Platforms",
        "",
        "| Platform | Games |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {name} | {count} |" for name, count in sorted(platforms.items()))
    lines.extend(["", "## Games", "", "| Title | Platform | Hours |", "| --- | --- | ---: |"])
    lines.extend(f"| {title} | {platform} | {hours:.1f} |" for title, platform, hours in games)
    return "\n".join(lines) + "\n"
