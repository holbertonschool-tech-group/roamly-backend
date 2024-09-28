# app/routes/destination_routes.py
from flask import Blueprint, request, jsonify
from app.models.destination import Destination
from app.database import db

destination_bp = Blueprint('destination_bp', __name__)

@destination_bp.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([destination.name for destination in destinations])

@destination_bp.route('/destinations', methods=['POST'])
def create_destination():
    data = request.json
    new_destination = Destination(name=data['name'], description=data['description'])
    db.session.add(new_destination)
    db.session.commit()
    return jsonify({'message': 'Destination created successfully'}), 201
