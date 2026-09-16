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


if __name__ == "__main__":
    unittest.main()
