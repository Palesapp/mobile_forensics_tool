import subprocess
import logging

# Initialize the logger
logger = logging.getLogger(__name__)

def extract_data(device_id):
    """
    Extract data from the mobile device using ADB (Android Debug Bridge).

    Args:
        device_id (str): The ID of the connected Android device.

    Returns:
        str: A message indicating the result of the data extraction.
    """
    if not device_id:
        logger.warning("Attempted data extraction with an invalid device ID.")
        return "Invalid device ID."
   
    try:
        logger.info(f"Starting data extraction for device ID: {device_id}")

        # Example command to extract SMS messages using ADB
        result = subprocess.run(
            ["adb", "-s", device_id, "shell", "content", "query", "--uri", "content://sms"],
            capture_output=True, text=True
        )

        if result.returncode == 0:
            # Successfully extracted data
            logger.info(f"Data extraction successful for device ID: {device_id}")
            return result.stdout  # or process the result as needed
        else:
            # Failed to extract data
            logger.error(f"Failed to extract data from device ID: {device_id}. Error: {result.stderr}")
            return "Failed to extract data from the device."
    except Exception as e:
        logger.exception(f"An error occurred during data extraction for device ID: {device_id}.")
        return f"An error occurred: {str(e)}"