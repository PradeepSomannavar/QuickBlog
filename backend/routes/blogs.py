import os
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from models import db, Blog, Comment
from services.email_service import send_email
from models import Subscriber

blogs_bp = Blueprint("blogs", __name__)

@blogs_bp.route("/", methods=["GET"])
def get_blogs():
    blogs = Blog.query.filter_by(status="published").all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "subtitle": b.subtitle,
        "thumbnail": b.thumbnail,
        "status": b.status,
        "created_at": b.created_at,
        "category_id": b.category_id
    } for b in blogs])

@blogs_bp.route("/admin", methods=["GET"])
@jwt_required()
def get_all_blogs():
    blogs = Blog.query.all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "subtitle": b.subtitle,
        "thumbnail": b.thumbnail,
        "status": b.status,
        "created_at": b.created_at.strftime("%d %b %Y"),
        "category_id": b.category_id
    } for b in blogs])

@blogs_bp.route("/<int:id>", methods=["GET"])
def get_blog(id):
    blog = Blog.query.get_or_404(id)
    return jsonify({
        "id": blog.id,
        "title": blog.title,
        "subtitle": blog.subtitle,
        "description": blog.description,
        "thumbnail": blog.thumbnail,
        "status": blog.status,
        "created_at": blog.created_at
    })

@blogs_bp.route("/", methods=["POST"])
@jwt_required()
def add_blog():
    try:
        filename = None
        if 'thumbnail' in request.files and request.files['thumbnail'].filename != '':
            file = request.files['thumbnail']
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.root_path, 'static', 'uploads', filename)
            file.save(upload_path)

        title = request.form.get('title')
        subtitle = request.form.get('subtitle')
        description = request.form.get('description')
        category_id = request.form.get('category_id')

        # Validate category_id is integer and exists
        if category_id is None or not category_id.isdigit():
            return jsonify({"error": "Invalid category_id"}), 400
        category_id_int = int(category_id)

        new_blog = Blog(
            title=title,
            subtitle=subtitle,
            description=description,
            thumbnail=filename,
            status="published",
            category_id=category_id_int
        )
        db.session.add(new_blog)
        db.session.commit()

        # Send notification emails to subscribers
        subscribers = Subscriber.query.all()
        emails = [sub.email for sub in subscribers]
        if emails:
            subject = f"New Blog Published: {title}"
            body = f"Hello,\n\nA new blog titled '{title}' has been published on QuickBlog.\n\nCheck it out on our website!\n\nBest regards,\nQuickBlog Team"
            send_email(subject, body, emails)

        return jsonify({"message": "Blog created"}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding blog: {e}")
        return jsonify({"error": "Failed to add blog", "details": str(e)}), 500

@blogs_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_blog(id):
    blog = Blog.query.get_or_404(id)
    data = request.get_json()
    if 'status' in data:
        blog.status = data['status']
    db.session.commit()
    return jsonify({"message": "Blog updated"})

@blogs_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_blog(id):
    blog = Blog.query.get_or_404(id)
    # Delete associated comments first
    Comment.query.filter_by(blog_id=id).delete()
    db.session.delete(blog)
    db.session.commit()
    return jsonify({"message": "Blog deleted"})
