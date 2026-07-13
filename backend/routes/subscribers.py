from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Subscriber

subscribers_bp = Blueprint("subscribers", __name__)

@subscribers_bp.route("/", methods=["POST"])
def subscribe():
    try:
        data = request.get_json()
        email = data.get("email")
        if not email:
            return jsonify({"error": "Email is required"}), 400

        existing = Subscriber.query.filter_by(email=email).first()
        if existing:
            if existing.active:
                return jsonify({"error": "Email already subscribed"}), 409
            existing.active = True
            db.session.commit()
            return jsonify({"message": "Subscription reactivated"}), 200

        new_sub = Subscriber(email=email, active=True)
        db.session.add(new_sub)
        db.session.commit()
        return jsonify({"message": "Subscribed successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@subscribers_bp.route("/", methods=["GET"])
@jwt_required()
def get_subscribers():
    subscribers = Subscriber.query.order_by(Subscriber.created_at.desc()).all()
    return jsonify([
        {"id": sub.id, "email": sub.email, "active": sub.active, "created_at": sub.created_at.isoformat() if sub.created_at else None}
        for sub in subscribers
    ])

@subscribers_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_subscriber(id):
    sub = Subscriber.query.get_or_404(id)
    db.session.delete(sub)
    db.session.commit()
    return jsonify({"message": "Subscriber deleted"})
