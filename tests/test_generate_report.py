import unittest
from app.generate_report import generate_report  # Ensure the path is correct

class TestGenerateReport(unittest.TestCase):

    def setUp(self):
        """
        Set up sample data for tests.
        """
        self.valid_data = {
            "sms_count": 2,
            "call_count": 1,
            "misc_info": "Some additional info"
        }

        self.empty_data = {}
        self.invalid_data = None

    def test_generate_report_with_valid_data(self):
        """
        Test report generation with valid data.
        """
        report = generate_report(self.valid_data)
        self.assertIn("Total SMS: 2", report)
        self.assertIn("Total Calls: 1", report)
        self.assertIn("misc_info: Some additional info", report)

    def test_generate_report_with_empty_data(self):
        """
        Test report generation with empty data.
        """
        report = generate_report(self.empty_data)
        self.assertEqual(report, "No data available to generate report.")

    def test_generate_report_with_invalid_data(self):
        """
        Test report generation with invalid data (None).
        """
        report = generate_report(self.invalid_data)
        self.assertEqual(report, "No data available to generate report.")

if __name__ == '__main__':
    unittest.main()