import unittest

from game_library_report.report import markdown_report


class ReportTests(unittest.TestCase):
    def test_report_contains_summary_and_rows(self):
        report = markdown_report(
            [{"title": "Hades", "platform": "PC", "hours_played": "12.5"}]
        )
        self.assertIn("**Games:** 1", report)
        self.assertIn("| Hades | PC | 12.5 |", report)

    def test_rejects_missing_title(self):
        with self.assertRaises(ValueError):
            markdown_report([{"platform": "PC"}])

    def test_filters_and_sorts_by_playtime(self):
        report = markdown_report(
            [
                {"title": "Short", "platform": "PC", "hours_played": "2"},
                {"title": "Long", "platform": "PC", "hours_played": "8"},
            ],
            min_hours=3,
            sort_by="hours",
        )
        self.assertNotIn("Short", report)
        self.assertIn("| Long | PC | 8.0 |", report)


if __name__ == "__main__":
    unittest.main()
