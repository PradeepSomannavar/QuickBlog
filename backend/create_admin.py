from models import db, User
from app import create_app
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    if not User.query.filter_by(username="pradeep").first():
        admin = User(
            username="pradeep",
            password_hash=generate_password_hash("pradeep123")
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
    else:
        print("Admin user already exists.")
