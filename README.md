# Game Library Report

Generate a readable Markdown report from a game-library CSV. The tool is
dependency-free and validates the required `title` column.

## Usage

```bash
python -m game_library_report games.csv
python -m game_library_report games.csv --output report.md
python -m game_library_report games.csv --min-hours 10 --sort-by hours
```

The CSV accepts `title`, `platform`, `genre`, `hours_played`, and `rating`.
Use `--min-hours` to focus on games above a playtime threshold, or `--sort-by`
to order the game table by title or hours played.
