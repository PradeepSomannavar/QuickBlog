from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models import Blog, Comment, Subscriber, Contact, PageView

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/stats", methods=["GET"])
@jwt_required()
def get_stats():
    total_blogs = Blog.query.count()
    total_drafts = Blog.query.filter_by(status="draft").count()
    total_published = Blog.query.filter_by(status="published").count()
    total_comments = Comment.query.count()
    total_pending_comments = Comment.query.filter_by(approved=False).count()
    total_subscribers = Subscriber.query.filter_by(active=True).count()
    total_messages = Contact.query.count()
    total_unread_messages = Contact.query.filter_by(is_read=False).count()

    total_page_views = PageView.query.count()
    total_blog_views = db.session.query(db.func.sum(Blog.views)).scalar() or 0

    return jsonify({
        "blogs": total_blogs,
        "drafts": total_drafts,
        "published": total_published,
        "comments": total_comments,
        "pending_comments": total_pending_comments,
        "subscribers": total_subscribers,
        "messages": total_messages,
        "unread_messages": total_unread_messages,
        "page_views": total_page_views,
        "total_visitors": total_blog_views + total_page_views,
    })
