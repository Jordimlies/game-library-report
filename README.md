# Game Library Report

Generate a readable Markdown report from a game-library CSV. The tool is
dependency-free and validates the required `title` column.

## Usage

```bash
python -m game_library_report games.csv
python -m game_library_report games.csv --output report.md
```

The CSV accepts `title`, `platform`, `genre`, `hours_played`, and `rating`.
