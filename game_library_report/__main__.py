import argparse
import csv
import sys

from .report import markdown_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Markdown game report.")
    parser.add_argument("csv_file")
    parser.add_argument("-o", "--output")
    parser.add_argument("--min-hours", type=float, default=0.0,
                        help="include only games with at least this many hours")
    parser.add_argument("--sort-by", choices=("title", "hours"),
                        help="sort the game table by title or playtime")
    args = parser.parse_args()

    try:
        with open(args.csv_file, newline="", encoding="utf-8") as stream:
            report = markdown_report(
                csv.DictReader(stream), min_hours=args.min_hours, sort_by=args.sort_by
            )
        if args.output:
            with open(args.output, "w", encoding="utf-8") as stream:
                stream.write(report)
        else:
            print(report, end="")
    except (OSError, csv.Error, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
