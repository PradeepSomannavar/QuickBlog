import os
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Blog, Comment, Subscriber, Tag
from services.email_service import send_email

blogs_bp = Blueprint("blogs", __name__)

def blog_to_dict(blog):
    return {
        "id": blog.id,
        "title": blog.title,
        "subtitle": blog.subtitle,
        "description": blog.description,
        "thumbnail": blog.thumbnail,
        "status": blog.status,
        "featured": blog.featured,
        "views": blog.views,
        "category_id": blog.category_id,
        "category_name": blog.category.name if blog.category else None,
        "tags": [{"id": t.id, "name": t.name} for t in blog.tags],
        "user_id": blog.user_id,
        "author": blog.author.username if blog.author else None,
        "created_at": blog.created_at.isoformat() if blog.created_at else None,
        "updated_at": blog.updated_at.isoformat() if blog.updated_at else None,
    }

@blogs_bp.route("/", methods=["GET"])
def get_blogs():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 12, type=int)
    category = request.args.get("category", type=int)
    featured_only = request.args.get("featured", type=bool)

    query = Blog.query.filter_by(status="published")

    if category:
        query = query.filter_by(category_id=category)
    if featured_only:
        query = query.filter_by(featured=True)

    query = query.order_by(Blog.created_at.desc())
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "blogs": [blog_to_dict(b) for b in pagination.items],
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page,
        "has_next": pagination.has_next,
        "has_prev": pagination.has_prev,
    })

@blogs_bp.route("/all", methods=["GET"])
def get_all_blogs_public():
    blogs = Blog.query.filter_by(status="published").order_by(Blog.created_at.desc()).all()
    return jsonify([blog_to_dict(b) for b in blogs])

@blogs_bp.route("/admin", methods=["GET"])
@jwt_required()
def get_all_blogs():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return jsonify([blog_to_dict(b) for b in blogs])

@blogs_bp.route("/<int:id>", methods=["GET"])
def get_blog(id):
    blog = Blog.query.get_or_404(id)
    blog.views = (blog.views or 0) + 1
    db.session.commit()
    return jsonify(blog_to_dict(blog))

@blogs_bp.route("/", methods=["POST"])
@jwt_required()
def add_blog():
    try:
        user_id = int(get_jwt_identity())

        filename = None
        if "thumbnail" in request.files and request.files["thumbnail"].filename:
            file = request.files["thumbnail"]
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.root_path, "static", "uploads", filename)
            file.save(upload_path)

        title = request.form.get("title")
        subtitle = request.form.get("subtitle")
        description = request.form.get("description")
        category_id = request.form.get("category_id")
        status = "published" if request.form.get("publish_now") == "true" else "draft"
        featured = request.form.get("featured") == "true"

        if category_id is None or not category_id.isdigit():
            return jsonify({"error": "Invalid category_id"}), 400

        new_blog = Blog(
            title=title,
            subtitle=subtitle,
            description=description,
            thumbnail=filename,
            status=status,
            featured=featured,
            category_id=int(category_id),
            user_id=user_id,
        )
        db.session.add(new_blog)
        db.session.commit()

        if status == "published":
            subscribers = Subscriber.query.filter_by(active=True).all()
            emails = [sub.email for sub in subscribers]
            if emails:
                subject = f"New Blog: {title}"
                body = (
                    f"Hello,\n\n"
                    f"A new blog titled '{title}' has been published on QuickBlog.\n\n"
                    f"Check it out on our website!\n\n"
                    f"Best regards,\nQuickBlog Team"
                )
                send_email(subject, body, emails)

        return jsonify({"message": "Blog created", "id": new_blog.id}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding blog: {e}")
        return jsonify({"error": "Failed to add blog", "details": str(e)}), 500

@blogs_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_blog(id):
    blog = Blog.query.get_or_404(id)
    data = request.get_json()
    if "title" in data:
        blog.title = data["title"]
    if "subtitle" in data:
        blog.subtitle = data["subtitle"]
    if "description" in data:
        blog.description = data["description"]
    if "category_id" in data:
        blog.category_id = data["category_id"]
    if "status" in data:
        blog.status = data["status"]
    if "featured" in data:
        blog.featured = data["featured"]
    db.session.commit()
    return jsonify({"message": "Blog updated"})

@blogs_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_blog(id):
    blog = Blog.query.get_or_404(id)
    Comment.query.filter_by(blog_id=id).delete()
    db.session.delete(blog)
    db.session.commit()
    return jsonify({"message": "Blog deleted"})
