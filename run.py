import logging
import sys
import os

# Add the current directory to the system path to ensure 'app' is found 
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app # Importing the app module

# Use 'development' as the default configuration
config_name = os.getenv('FLASK_ENV', 'development')

app = create_app('development')

if __name__ == '__main__':
    app.run(debug=True) # Force debug mode here