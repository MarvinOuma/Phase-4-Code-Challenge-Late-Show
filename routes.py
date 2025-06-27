from flask import Blueprint, request, jsonify
from app import db
from models import Episode, Guest, Appearance
from sqlalchemy.exc import IntegrityError

main_bp = Blueprint('main', __name__)

@main_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@main_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict(include_appearances=True))

@main_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@main_bp.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    errors = []

    if rating is None or not (1 <= rating <= 5):
        errors.append("Rating must be between 1 and 5")
    if episode_id is None:
        errors.append("episode_id is required")
    if guest_id is None:
        errors.append("guest_id is required")

    if errors:
        return jsonify({"errors": errors}), 400

    episode = Episode.query.get(episode_id)
    if not episode:
        return jsonify({"errors": ["Episode not found"]}), 400

    guest = Guest.query.get(guest_id)
    if not guest:
        return jsonify({"errors": ["Guest not found"]}), 400

    try:
        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(appearance)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Database error"]}), 400
    except ValueError as ve:
        return jsonify({"errors": [str(ve)]}), 400

    response = appearance.to_dict(include_guest=True, include_episode=True)
    return jsonify(response), 201
