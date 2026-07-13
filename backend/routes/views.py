from flask import Blueprint, request, jsonify
from models import db, PageView, Blog

views_bp = Blueprint("views", __name__)


@views_bp.route("/track", methods=["POST"])
def track_view():
    data = request.get_json()
    blog_id = data.get("blog_id")

    page_view = PageView(
        blog_id=blog_id,
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent"),
    )
    db.session.add(page_view)
    db.session.commit()

    return jsonify({"message": "View tracked"}), 201


@views_bp.route("/stats", methods=["GET"])
def get_view_stats():
    total_views = PageView.query.count()
    unique_ips = (
        db.session.query(PageView.ip_address)
        .distinct()
        .count()
    )
    return jsonify({
        "total_views": total_views,
        "unique_visitors": unique_ips,
    })
