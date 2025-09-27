from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
from models import db
from config import Config
from routes.ai import ai_bp

load_dotenv()



# Blueprints
from routes.auth import auth_bp
from routes.blogs import blogs_bp
from routes.comments import comments_bp
from routes.subscribers import subscribers_bp
from routes.dashboard import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(blogs_bp, url_prefix="/api/blogs")
    app.register_blueprint(comments_bp, url_prefix="/api/comments")
    app.register_blueprint(subscribers_bp, url_prefix="/api/subscribers")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(ai_bp, url_prefix="/api/ai")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
