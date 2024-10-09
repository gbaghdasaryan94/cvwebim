from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os

db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    Session(app)
    db.init_app(app)
    
    with app.app_context():
        # Imports
        from . import routes
        
        # Create tables for our models
        dbpath = os.path.abspath('survey.db')
        if not os.path.exists(dbpath):  # Check for the survey.db database file
            # Create tables for our models
            db.create_all()
            print("-----------------Database created!--------------------------------")
        else:
            print("Database already exists. Skipping creation.")
        
        #Check if tables exist 
        existing_tables = db.metadata.tables.keys()
        print("Existing tables:", list(existing_tables))
        
        #  Specify the tables you expect to exist
        expected_tables = ['users', 'ewi_info', 'skill_info']  # List of expected table names

            # Create tables that do not exist
        for table in expected_tables:
            if table not in existing_tables:
                db.create_all()
                print(f"Table '{table}' created.")
            else:
                print(f"Table '{table}' already exists.")
        
        return app
