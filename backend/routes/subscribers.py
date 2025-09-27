from flask import Blueprint, request, jsonify
from models import db, Subscriber

subscribers_bp = Blueprint("subscribers", __name__)

@subscribers_bp.route("/", methods=["POST"])
def subscribe():
    try:
        data = request.get_json()
        email = data.get("email")
        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Check if email already subscribed
        existing = Subscriber.query.filter_by(email=email).first()
        if existing:
            return jsonify({"error": "Email already subscribed"}), 409

        new_sub = Subscriber(email=email)
        db.session.add(new_sub)
        db.session.commit()
        return jsonify({"message": "Subscribed successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@subscribers_bp.route("/", methods=["GET"])
def get_subscribers():
    subscribers = Subscriber.query.all()
    print(f"DEBUG: Fetched {len(subscribers)} subscribers from DB")
    for sub in subscribers:
        print(f"DEBUG: Subscriber - id: {sub.id}, email: {sub.email}")
    result = [{"id": sub.id, "email": sub.email} for sub in subscribers]
    return jsonify(result)

@subscribers_bp.route("/<int:id>", methods=["DELETE"])
def delete_subscriber(id):
    sub = Subscriber.query.get_or_404(id)
    db.session.delete(sub)
    db.session.commit()
    return jsonify({"message": "Subscriber deleted"})
