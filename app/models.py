import logging
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import db # Import the db instance from __init__.py

# Initialize the logger
logger = logging.getLogger(__name__)

db = SQLAlchemy()

class ExtractedData(db.Model):
    __tablename__ = 'extracted_data'
   
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(64), nullable=False)
    extraction_date = db.Column(db.DateTime, default=datetime.utcnow)
    data_type = db.Column(db.String(64), nullable=False)  # e.g., 'SMS', 'Call Logs', 'Contacts'
    raw_data = db.Column(db.Text, nullable=False)

    def __init__(self, device_id, data_type, raw_data):
        self.device_id = device_id
        self.data_type = data_type
        self.raw_data = raw_data
        try:
            logger.info(f"New ExtractedData created: Device ID: {self.device_id}, Data Type: {self.data_type}")
        except Exception as e:
            logger.error(f"Error during ExtractedData creation: {str(e)}")

    def __repr__(self):
        return f"<ExtractedData {self.device_id} - {self.data_type}>"

class CommunicationAnalysis(db.Model):
    __tablename__ = 'communication_analysis'
   
    id = db.Column(db.Integer, primary_key=True)
    extracted_data_id = db.Column(db.Integer, db.ForeignKey('extracted_data.id'), nullable=False)
    analysis_date = db.Column(db.DateTime, default=datetime.utcnow)
    analysis_result = db.Column(db.Text, nullable=False)
   
    extracted_data = db.relationship('ExtractedData', backref=db.backref('analyses', lazy=True))

    def __init__(self, extracted_data_id, analysis_result):
        self.extracted_data_id = extracted_data_id
        self.analysis_result = analysis_result
        try:
            logger.info(f"New CommunicationAnalysis created for Extracted Data ID: {self.extracted_data_id}")
        except Exception as e:
            logger.error(f"Error during CommunicationAnalysis creation: {str(e)}")

    def __repr__(self):
        return f"<CommunicationAnalysis {self.id} - {self.analysis_date}>"