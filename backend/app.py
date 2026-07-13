from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db
from config import Config

from routes.auth import auth_bp
from routes.blogs import blogs_bp
from routes.comments import comments_bp
from routes.subscribers import subscribers_bp
from routes.dashboard import dashboard_bp
from routes.ai import ai_bp
from routes.categories import categories_bp
from routes.contacts import contacts_bp
from routes.settings import settings_bp
from routes.views import views_bp
from routes.search import search_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(blogs_bp, url_prefix="/api/blogs")
    app.register_blueprint(comments_bp, url_prefix="/api/comments")
    app.register_blueprint(subscribers_bp, url_prefix="/api/subscribers")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(ai_bp, url_prefix="/api/ai")
    app.register_blueprint(categories_bp, url_prefix="/api/categories")
    app.register_blueprint(contacts_bp, url_prefix="/api/contacts")
    app.register_blueprint(settings_bp, url_prefix="/api/settings")
    app.register_blueprint(views_bp, url_prefix="/api/views")
    app.register_blueprint(search_bp, url_prefix="/api/search")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
