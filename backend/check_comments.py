from models import db, Comment
from app import create_app

app = create_app()

with app.app_context():
    comments = Comment.query.all()
    print(f"Total comments: {len(comments)}")
    for comment in comments:
        print(f"ID: {comment.id}, Blog ID: {comment.blog_id}, Name: {comment.name}, Comment: {comment.comment}, Approved: {comment.approved}, Created: {comment.created_at}")
