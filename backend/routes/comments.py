from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Comment

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/", methods=["POST"])
def add_comment():
    data = request.get_json()
    new_comment = Comment(
        blog_id=data["blog_id"],
        name=data["name"],
        comment=data["comment"],
        approved=True  # Auto-approve comments for immediate display
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment added successfully"}), 201

@comments_bp.route("/", methods=["GET"])
@jwt_required()
def get_comments():
    comments = Comment.query.all()
    return jsonify([{
        "id": c.id,
        "blog_id": c.blog_id,
        "name": c.name,
        "comment": c.comment,
        "approved": c.approved,
        "created_at": c.created_at
    } for c in comments])

@comments_bp.route("/public", methods=["GET"])
def get_public_comments():
    comments = Comment.query.filter_by(approved=True).all()
    return jsonify([{
        "id": c.id,
        "blog_id": c.blog_id,
        "name": c.name,
        "comment": c.comment,
        "approved": c.approved,
        "created_at": c.created_at
    } for c in comments])

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
    if 'name' in data:
        comment.name = data['name']
    if 'comment' in data:
        comment.comment = data['comment']
    db.session.commit()
    return jsonify({"message": "Comment updated"})

@comments_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"})
