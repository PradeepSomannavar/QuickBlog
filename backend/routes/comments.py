from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Comment

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/", methods=["POST"])
def add_comment():
    data = request.get_json()
    if not data.get("blog_id") or not data.get("name") or not data.get("comment"):
        return jsonify({"error": "blog_id, name, and comment are required"}), 400
    new_comment = Comment(
        blog_id=data["blog_id"],
        name=data["name"],
        email=data.get("email"),
        comment=data["comment"],
        approved=True,
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment added successfully", "id": new_comment.id}), 201

@comments_bp.route("/", methods=["GET"])
@jwt_required()
def get_comments():
    blog_id = request.args.get("blog_id", type=int)
    query = Comment.query
    if blog_id:
        query = query.filter_by(blog_id=blog_id)
    comments = query.order_by(Comment.created_at.desc()).all()
    return jsonify([
        {
            "id": c.id,
            "blog_id": c.blog_id,
            "name": c.name,
            "email": c.email,
            "comment": c.comment,
            "approved": c.approved,
            "created_at": c.created_at.isoformat() if c.created_at else None,
        }
        for c in comments
    ])

@comments_bp.route("/public", methods=["GET"])
def get_public_comments():
    blog_id = request.args.get("blog_id", type=int)
    query = Comment.query.filter_by(approved=True)
    if blog_id:
        query = query.filter_by(blog_id=blog_id)
    comments = query.order_by(Comment.created_at.desc()).all()
    return jsonify([
        {
            "id": c.id,
            "blog_id": c.blog_id,
            "name": c.name,
            "comment": c.comment,
            "created_at": c.created_at.isoformat() if c.created_at else None,
        }
        for c in comments
    ])

@comments_bp.route("/<int:id>/approve", methods=["PUT"])
@jwt_required()
def approve_comment(id):
    comment = Comment.query.get_or_404(id)
    comment.approved = True
    db.session.commit()
    return jsonify({"message": "Comment approved"})

@comments_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_comment(id):
    comment = Comment.query.get_or_404(id)
    data = request.get_json()
    if "name" in data:
        comment.name = data["name"]
    if "comment" in data:
        comment.comment = data["comment"]
    db.session.commit()
    return jsonify({"message": "Comment updated"})

@comments_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"})
