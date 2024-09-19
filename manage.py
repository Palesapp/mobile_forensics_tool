from flask import Flask
from flask_migrate import Migrate
from app import create_app, db #import create_app and db
from flask.cli import FlaskGroup

# Create the Flask application
app = create_app()
migrate = Migrate(app, db)

# Define a CLI group
cli = FlaskGroup(create_app=create_app)

# Register Flask-Migrate commands
@cli.command("db")
def db_command():
    """Run database migrations."""
    from flask.cli import main as flask_main
    flask_main(argv=["db", "init"])  # or other db commands

if __name__ == '__main__':
    cli()