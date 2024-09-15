import unittest
from unittest.mock import patch
from app.extract_data import extract_data  # Ensure the path is correct

class TestExtractData(unittest.TestCase):

    def setUp(self):
        """
        Set up any shared state between tests.
        """
        self.valid_device_id = "1234567890abcdef"
        self.invalid_device_id = ""

    @patch('subprocess.run')
    def test_extract_data_with_valid_device(self, mock_run):
        """
        Test data extraction with a valid device ID.
        """
        # Mocking the subprocess.run call to simulate successful data extraction
        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = "SMS data extracted."

        result = extract_data(self.valid_device_id)
        self.assertEqual(result, "SMS data extracted.")

    @patch('subprocess.run')
    def test_extract_data_with_invalid_device(self, mock_run):
        """
        Test data extraction with an invalid device ID.
        """
        result = extract_data(self.invalid_device_id)
        self.assertEqual(result, "Invalid device ID.")

    @patch('subprocess.run')
    def test_extract_data_failure(self, mock_run):
        """
        Test failure scenario of data extraction.
        """
        # Simulating a failure in data extraction
        mock_run.return_value.returncode = 1

        result = extract_data(self.valid_device_id)
        self.assertEqual(result, "Failed to extract data from the device.")

if __name__ == '__main__':
    unittest.main()