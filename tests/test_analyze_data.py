import unittest
from app.analyze_data import analyze_data  # Make sure this path is correct based on your project structure

class TestAnalyzeData(unittest.TestCase):

    def setUp(self):
        """
        This method is run before each test to set up any state that's shared between tests.
        """
        # Example of valid data for analysis
        self.valid_data = [
            {"type": "sms", "content": "Hey there!", "timestamp": "2024-09-08 12:00"},
            {"type": "call", "duration": "120", "timestamp": "2024-09-07 10:30"},
            {"type": "sms", "content": "Meeting at 3PM", "timestamp": "2024-09-07 08:45"}
        ]

        # Example of invalid data (empty or None)
        self.invalid_data = None

    def test_successful_data_analysis(self):
        """
        Test data analysis with valid data.
        """
        result = analyze_data(self.valid_data)
        self.assertIsNotNone(result)  # Ensure result is not None
        self.assertIsInstance(result, dict)  # Expecting the result to be a dictionary
        self.assertIn('sms_count', result)  # Example: Check if 'sms_count' key is in the result
        self.assertEqual(result['sms_count'], 2)  # Check if the sms count is correct

    def test_empty_data_analysis(self):
        """
        Test data analysis with no data or empty input.
        """
        result = analyze_data([])
        self.assertIsInstance(result, dict)  # Expecting a dictionary result even with no data
        self.assertEqual(result.get('sms_count', 0), 0)  # Expect sms_count to be 0 when no data

    def test_invalid_data_analysis(self):
        """
        Test data analysis with invalid data (None).
        """
        result = analyze_data(self.invalid_data)
        self.assertIsInstance(result, dict)  # Expect a dictionary even for invalid data
        self.assertEqual(result, {})  # Expect the result to be an empty dictionary

if __name__ == '__main__':
    unittest.main()