import logging

# Initialize the logger
logger = logging.getLogger(__name__)

def generate_report(data):
    """
    Generate a report based on the analyzed data.

    Args:
        data (dict): A dictionary containing analysis data.

    Returns:
        str: A formatted report string.
    """
    if not isinstance(data, dict) or not data:
        logger.warning("Attempted to generate report with invalid or empty data.")
        return "No data available to generate report."
    
    logger.info("Generating report based on the analyzed data.")
   
    report = []
   
    # Example of creating a simple report
    report.append(f"Report Generated:")
    report.append(f"Total SMS: {data.get('sms_count', 0)}")
    report.append(f"Total Calls: {data.get('call_count', 0)}")
   
    logger.info(f"Total SMS: {data.get('sms_count', 0)}")
    logger.info(f"Total Calls: {data.get('call_count', 0)}")
   
    # Adding more details based on data
    for key, value in data.items():
        if key not in ['sms_count', 'call_count']:
            report.append(f"{key}: {value}")
            logger.info(f"{key}: {value}")

    logger.info("Report generation completed.")
    return "\n".join(report)