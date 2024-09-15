import logging

# Initialize the logger
logger = logging.getLogger(__name__)

def analyze_data(data):
    """
    A function to analyze data and return some statistics.
    """
    if not data or not isinstance(data, list):
        logger.warning("Invalid data received for analysis. Returning empty dictionary.")
        return {}  # Return an empty dictionary instead of None

    try:
        # Log the size of the dataset being analyzed
        logger.info(f"Analyzing data: {len(data)} entries.")

        # Calculate SMS and Call counts
        sms_count = sum(1 for entry in data if entry.get('type') == 'sms')
        call_count = sum(1 for entry in data if entry.get('type') == 'call')

        logger.info(f"Analysis complete: {sms_count} SMS entries, {call_count} Call entries.")

        return {
            'sms_count': sms_count,
            'call_count': call_count
        }
    
    except Exception as e:
        # Log any exceptions that occur during analysis
        logger.error(f"Error occurred during data analysis: {str(e)}")
        return {}