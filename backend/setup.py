"""
QuickBlog Setup Script
======================
Creates the MySQL database, initializes all tables,
and seeds default data.
"""

import pymysql
from app import create_app
from models import db

DB_NAME = "quickblog"
DB_USER = "root"
DB_PASSWORD = "password"
DB_HOST = "localhost"


def create_database():
    """Create the MySQL database if it doesn't exist."""
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"[OK] Database '{DB_NAME}' ready.")
        connection.close()
    except pymysql.err.OperationalError as e:
        print(f"[FAIL] MySQL connection failed: {e}")
        print("    Make sure MySQL is running on localhost:3306")
        exit(1)


def create_tables():
    """Create all tables."""
    app = create_app()
    with app.app_context():
        db.create_all()
        print("[OK] All tables created.")
    return app


def seed_data(app):
    """Seed default data."""
    from models import User, Category, SiteSetting
    from werkzeug.security import generate_password_hash

    with app.app_context():
        # Admin user
        if not User.query.filter_by(username="pradeep").first():
            admin = User(
                username="pradeep",
                email="admin@quickblog.com",
                password_hash=generate_password_hash("pradeep123"),
                role="admin"
            )
            db.session.add(admin)
            db.session.commit()
            print("[OK] Admin user: pradeep / pradeep123")
        else:
            print("[*] Admin user already exists.")

        # Categories
        categories = [
            {"name": "Tech", "slug": "tech", "description": "Technology news and tutorials"},
            {"name": "AI", "slug": "ai", "description": "Artificial Intelligence and machine learning"},
            {"name": "Lifestyle", "slug": "lifestyle", "description": "Health, wellness, and lifestyle"},
            {"name": "Finance", "slug": "finance", "description": "Personal finance and investing"},
            {"name": "Design", "slug": "design", "description": "UI/UX and creative design"},
            {"name": "Science", "slug": "science", "description": "Scientific discoveries"},
        ]
        for cat in categories:
            if not Category.query.filter_by(name=cat["name"]).first():
                db.session.add(Category(**cat))
        db.session.commit()
        print(f"[OK] {len(categories)} categories created.")

        # Default settings
        default_settings = {
            "site_name": "QuickBlog",
            "site_description": "A modern blog platform for insightful stories.",
            "footer_text": "QuickBlog. All rights reserved.",
            "contact_email": "contact@quickblog.com",
            "contact_phone": "+1 (555) 123-4567",
        }
        for key, value in default_settings.items():
            if not SiteSetting.query.filter_by(key=key).first():
                db.session.add(SiteSetting(key=key, value=value))
        db.session.commit()
        print("[OK] Default settings saved.")

    print("\n[OK] Setup complete! Run 'python app.py' to start the server.")


if __name__ == "__main__":
    print("=" * 50)
    print("  QuickBlog — Database Setup")
    print("=" * 50)

    create_database()
    app = create_tables()
    seed_data(app)
