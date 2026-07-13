from app import create_app
from models import db, Category

app = create_app()

categories_data = [
    {"name": "Tech", "slug": "tech", "description": "Technology news, reviews, and tutorials"},
    {"name": "AI", "slug": "ai", "description": "Artificial Intelligence, machine learning, and data science"},
    {"name": "Lifestyle", "slug": "lifestyle", "description": "Health, wellness, travel, and personal development"},
    {"name": "Finance", "slug": "finance", "description": "Personal finance, investing, and economic insights"},
    {"name": "Design", "slug": "design", "description": "UI/UX, graphic design, and creative inspiration"},
    {"name": "Science", "slug": "science", "description": "Scientific discoveries and research"},
]

with app.app_context():
    for cat in categories_data:
        if not Category.query.filter_by(name=cat["name"]).first():
            db.session.add(Category(**cat))
    db.session.commit()
    print(f"Default categories added successfully!")
