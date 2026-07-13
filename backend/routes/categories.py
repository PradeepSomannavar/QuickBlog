from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Category

categories_bp = Blueprint("categories", __name__)


@categories_bp.route("/", methods=["GET"])
def get_categories():
    categories = Category.query.order_by(Category.name).all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "slug": c.slug,
            "description": c.description,
        }
        for c in categories
    ])


@categories_bp.route("/", methods=["POST"])
@jwt_required()
def add_category():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    if Category.query.filter_by(name=name).first():
        return jsonify({"error": "Category already exists"}), 409

    category = Category(
        name=name,
        slug=name.lower().replace(" ", "-"),
        description=data.get("description"),
    )
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": "Category created", "id": category.id}), 201


@categories_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_category(id):
    category = Category.query.get_or_404(id)
    data = request.get_json()
    if "name" in data:
        category.name = data["name"]
        category.slug = data["name"].lower().replace(" ", "-")
    if "description" in data:
        category.description = data["description"]
    db.session.commit()
    return jsonify({"message": "Category updated"})


@categories_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted"})
