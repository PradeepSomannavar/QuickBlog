from app import create_app
from models import db, Category

app = create_app()

with app.app_context():
    categories = ["Tech", "AI", "Lifestyle", "Finance"]

    for name in categories:
        if not Category.query.filter_by(name=name).first():
            db.session.add(Category(name=name))

    db.session.commit()
    print("Default categories added successfully!")
