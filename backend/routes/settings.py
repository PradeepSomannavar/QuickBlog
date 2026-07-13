from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, SiteSetting

settings_bp = Blueprint("settings", __name__)

DEFAULT_SETTINGS = {
    "site_name": "QuickBlog",
    "site_description": "A modern blog platform for insightful stories.",
    "footer_text": "QuickBlog. All rights reserved.",
    "social_facebook": "#",
    "social_twitter": "#",
    "social_instagram": "#",
    "social_linkedin": "#",
    "contact_email": "contact@quickblog.com",
    "contact_phone": "+1 (555) 123-4567",
    "blogs_per_page": "12",
}


@settings_bp.route("/", methods=["GET"])
def get_settings():
    settings = SiteSetting.query.all()
    result = {s.key: s.value for s in settings}
    for key, val in DEFAULT_SETTINGS.items():
        if key not in result:
            result[key] = val
    return jsonify(result)


@settings_bp.route("/", methods=["PUT"])
@jwt_required()
def update_settings():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    for key, value in data.items():
        setting = SiteSetting.query.filter_by(key=key).first()
        if setting:
            setting.value = str(value)
        else:
            setting = SiteSetting(key=key, value=str(value))
            db.session.add(setting)

    db.session.commit()
    return jsonify({"message": "Settings updated successfully"})
