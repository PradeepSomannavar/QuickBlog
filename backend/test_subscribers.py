from app import create_app
from models import db, Subscriber

app = create_app()

with app.app_context():
    try:
        subscribers = Subscriber.query.all()
        print(f"Found {len(subscribers)} subscribers:")
        for sub in subscribers:
            print(f"ID: {sub.id}, Email: {sub.email}")
    except Exception as e:
        print("Error querying subscribers:", e)
