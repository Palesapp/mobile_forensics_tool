import logging
from flask import Blueprint, render_template, send_file, request
import os
import pdfkit

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Log debug information

# Log to a file and the console
file_handler = logging.FileHandler('app.log')
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Define the blueprint
main = Blueprint('main', __name__)

# Default route
@main.route('/')
def index():
    logger.info("Accessed the index page.")
    return render_template('index.html')  # Ensure this template exists in your 'templates' folder

# Route to generate a report and save it as a PDF
@main.route('/generate_report', methods=['GET', 'POST'])
def generate_report():
    data = {'key': 'value'}  # Replace with the actual data to pass into the report
    rendered = render_template('report_template.html', data=data)  # Render the HTML template

    # Specify the path where the PDF will be saved
    pdf_path = os.path.join(os.getcwd(), 'GeneratedReports', 'report.pdf')

    # Ensure the directory exists before generating the PDF
    if not os.path.exists(os.path.dirname(pdf_path)):
        os.makedirs(os.path.dirname(pdf_path))

    try:
        pdfkit.from_string(rendered, pdf_path)  # Generate the PDF
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Could not find the PDF at {pdf_path}")

        logger.info(f"PDF report generated successfully at {pdf_path}.")
        return send_file(pdf_path, as_attachment=True)
   
    except Exception as e:
        logger.error(f"An error occurred while generating the report: {str(e)}")
        return f"An error occurred: {str(e)}"

# Route for extracting data
@main.route('/extract_data', methods=['GET', 'POST'])
def extract_data():
    if request.method == 'POST':
        logger.info("Data extraction initiated.")
        message = extract_android_data()  # Call the extraction function
        logger.info("Data extraction completed successfully.")
        return render_template('extract_data.html', message=message)
    logger.info("Accessed the data extraction page.")
    return render_template('extract_data.html')

# Route for analyzing data
@main.route('/analyze_data', methods=['GET', 'POST'])
def analyze_data():
    if request.method == 'POST':
        logger.info("Data analysis initiated.")
        analysis_result = analyze_android_data()  # Call the analysis function
        logger.info("Data analysis completed successfully.")
        return render_template('analysis_of_communication.html', result=analysis_result)
    logger.info("Accessed the data analysis page.")
    return render_template('analysis_of_communication.html')

# Function for extracting data (replace with actual logic)
def extract_android_data():
    logger.debug("Starting data extraction logic.")
    return "Data extraction complete!"

# Function for analyzing data (replace with actual logic)
def analyze_android_data():
    logger.debug("Starting data analysis logic.")
    analysis_result = "Analysis complete! Data shows interesting communication patterns."
    return analysis_result