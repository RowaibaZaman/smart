# create_tables.py
from app import create_app

app = create_app()

with app.app_context():
    print("Tables created successfully")