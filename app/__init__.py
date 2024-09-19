import os
import logging
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize database and migration objects
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')

    print(f"FLASK_ENV: {config_name}")

    # Create and configure the Flask app
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Log the database URI for debugging purposes
    app.logger.info(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    register_blueprints(app)

    return app

def register_blueprints(app):
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

def setup_logging(app):
    # Clear existing loggers to avoid duplicate logs
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    log_level = logging.DEBUG if app.config['DEBUG'] else logging.INFO

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

    app.logger.info("Logging setup complete.")

# Call setup_logging once during app initialization
setup_logging(app)