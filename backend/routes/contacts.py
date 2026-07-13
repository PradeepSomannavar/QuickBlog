from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Contact

contacts_bp = Blueprint("contacts", __name__)


@contacts_bp.route("/", methods=["POST"])
def submit_contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "Name, email, and message are required"}), 400

    contact = Contact(
        name=name,
        email=email,
        phone=data.get("phone"),
        subject=data.get("subject"),
        message=message,
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({"message": "Message sent successfully", "id": contact.id}), 201


@contacts_bp.route("/", methods=["GET"])
@jwt_required()
def get_contacts():
    contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "phone": c.phone,
            "subject": c.subject,
            "message": c.message,
            "is_read": c.is_read,
            "created_at": c.created_at.isoformat() if c.created_at else None,
        }
        for c in contacts
    ])


@contacts_bp.route("/<int:id>/read", methods=["PUT"])
@jwt_required()
def mark_as_read(id):
    contact = Contact.query.get_or_404(id)
    contact.is_read = True
    db.session.commit()
    return jsonify({"message": "Marked as read"})


@contacts_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact deleted"})
