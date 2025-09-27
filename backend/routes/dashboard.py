from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import Blog, Comment, Subscriber

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/stats", methods=["GET"])
@jwt_required()
def get_stats():
    total_blogs = Blog.query.count()
    total_drafts = Blog.query.filter_by(status="draft").count()
    total_comments = Comment.query.count()
    total_subscribers = Subscriber.query.count()

    # Fetch recent blogs (latest 5)
    recent_blogs = Blog.query.order_by(Blog.created_at.desc()).limit(5).all()
    recent_blogs_data = [
        {
            "id": blog.id,
            "title": blog.title,
            "created_at": blog.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "status": blog.status
        }
        for blog in recent_blogs
    ]

    # TODO: Implement visitor tracking and get total visitors count
    total_visitors = 0

    # Fetch recent comments (latest 5)
    recent_comments = Comment.query.order_by(Comment.created_at.desc()).limit(5).all()
    recent_comments_data = [
        {
            "id": comment.id,
            "blog_id": comment.blog_id,
            "name": comment.name,
            "comment": comment.comment,
            "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "approved": comment.approved
        }
        for comment in recent_comments
    ]

    return jsonify({
        "blogs": total_blogs,
        "drafts": total_drafts,
        "comments": total_comments,
        "subscribers": total_subscribers,
        "recent_blogs": recent_blogs_data,
        "recent_comments": recent_comments_data,
        "total_visitors": total_visitors
    })
