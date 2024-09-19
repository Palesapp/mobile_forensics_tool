import os
import logging
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create instances of the database and migration
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # Load the appropriate config

    # Initialize the database and migration with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints here to avoid circular imports
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

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