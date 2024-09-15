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
    # Clear any existing loggers to avoid duplicate logs
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Set logging level based on the environment
    log_level = logging.DEBUG if app.config['DEBUG'] else logging.INFO

    # Set up logging format to ensure it's consistent
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]  # Log to the console (stdout)
    )

    # Log the environment mode
    logging.info(f"Starting application in {app.config['ENV']} mode")

    # Additional error logging for production environments
    if not app.config['DEBUG']:
        # Log errors to stderr
        logging.getLogger('werkzeug').setLevel(logging.ERROR)  # Reducing Werkzeug logging to errors only in production
        logging.error("Logging setup complete. Errors will be logged.")