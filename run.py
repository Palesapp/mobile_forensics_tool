import logging
import sys
import os

# Check if we're on a Windows system (os.name == 'nt'), and skip 'fcntl' import if true
if os.name != 'nt':  # 'nt' indicates Windows, and 'posix' indicates Linux/Unix
    try:
        import fcntl
    except ImportError:
        logging.warning("fcntl not available on this system (Windows), continuing without it.")

# Add the current directory to the system path to ensure 'app' is found
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from app import create_app  # Importing the app module
except ImportError as e:
    logging.error(f"Error importing create_app from app: {e}")
    raise

# Use environment variable 'FLASK_ENV' if set, otherwise default to 'development'
config_name = os.getenv('FLASK_ENV', 'development')

# Create the app instance
try:
    app = create_app(config_name)
except Exception as e:
    logging.error(f"Error during app creation: {e}")
    raise

# Set up logging
logging.basicConfig(level=logging.DEBUG)  # Set to DEBUG for more detailed output

if __name__ == '__main__':
    try:
        app.run(debug=True)  # Forcing debug mode in development
    except Exception as e:
        logging.error(f"Error running the app: {e}")
        raise