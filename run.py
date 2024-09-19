from app import create_app
import logging
import sys
import os

# Add the current directory to the system path to ensure 'app' is found
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Set to DEBUG for more detailed output

# Use environment variable 'FLASK_ENV' if set, otherwise default to 'development'
config_name = os.getenv('FLASK_ENV', 'development')

# Create the Flask application
try:
    app = create_app(config_name)
except ImportError as e:
    logging.error(f"Error importing create_app from app: {e}")
    sys.exit(1)  # Exit if there's an import error
except Exception as e:
    logging.error(f"Error during app creation: {e}")
    sys.exit(1)  # Exit if there's an error during app creation

if __name__ == '__main__':
    # Run the app
    try:
        app.run(debug=True)  # Forcing debug mode in development
    except Exception as e:
        logging.error(f"Error running the app: {e}")
        sys.exit(1)  # Exit if there's an error while running the app