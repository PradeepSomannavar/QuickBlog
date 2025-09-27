from models import db
from app import create_app

app = create_app()

with app.app_context():
    try:
        db.create_all()
        print("Database connected and tables created successfully!")
    except Exception as e:
        print("DB connection failed:", e)
