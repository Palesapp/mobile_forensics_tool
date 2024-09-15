from app import app, db  # Import both the app and the db

# Set up the application context
with app.app_context():
    db.create_all()  # Create the database tables