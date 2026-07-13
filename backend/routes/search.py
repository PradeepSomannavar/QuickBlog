from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from models import db, Blog

search_bp = Blueprint("search", __name__)


@search_bp.route("/", methods=["GET"])
def search():
    q = request.args.get("q", "").strip()
    category = request.args.get("category", type=int)
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 12, type=int)

    if not q and not category:
        return jsonify({"error": "Search query or category required"}), 400

    query = Blog.query.filter_by(status="published")

    if q:
        like = f"%{q}%"
        query = query.filter(
            or_(Blog.title.ilike(like), Blog.subtitle.ilike(like), Blog.description.ilike(like))
        )

    if category:
        query = query.filter_by(category_id=category)

    query = query.order_by(Blog.created_at.desc())
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "blogs": [
            {
                "id": b.id,
                "title": b.title,
                "subtitle": b.subtitle,
                "thumbnail": b.thumbnail,
                "category_id": b.category_id,
                "category_name": b.category.name if b.category else None,
                "created_at": b.created_at.isoformat() if b.created_at else None,
            }
            for b in pagination.items
        ],
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page,
    })
