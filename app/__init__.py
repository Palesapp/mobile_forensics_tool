import os
import logging
from flask import Flask
from config import config  # Ensure you're importing 'config' from config.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize database and migration objects
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')  # Defaults to 'development' if FLASK_ENV is not set
    
    print(f"FLASK_ENV: {config_name}")  # This will print the current environment in the console

    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Set up logging
    setup_logging(app)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def setup_logging(app):
    # Set logging level based on the environment
    if app.config['DEBUG']:
        logging.basicConfig(level=logging.DEBUG)  # Log more detailed information for debugging
    else:
        logging.basicConfig(level=logging.INFO)   # Less detailed logging for production

    # Example of custom logging
    logging.info(f"Starting application in {app.config['ENV']} mode")
    
    # Logging errors
    logging.error("An example error log")
    
    # You can log other levels as needed (debug, warning, etc.)