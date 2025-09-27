from app import app, db
from models import Blog

with app.app_context():
    drafts = Blog.query.filter_by(status="draft").all()
    for blog in drafts:
        blog.status = "published"
    db.session.commit()
    print(f"Updated {len(drafts)} drafts to published")
