import argparse
import csv
import sys

from .report import markdown_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Markdown game report.")
    parser.add_argument("csv_file")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    try:
        with open(args.csv_file, newline="", encoding="utf-8") as stream:
            report = markdown_report(csv.DictReader(stream))
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
