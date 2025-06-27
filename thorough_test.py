import json
from app import create_app, db
from models import Episode, Guest, Appearance

def run_tests():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        # Seed test data
        episode1 = Episode(number=1, date="1/11/99")
        episode2 = Episode(number=2, date="1/12/99")
        guest1 = Guest(name="Michael J. Fox", occupation="actor")
        guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
        guest3 = Guest(name="Tracey Ullman", occupation="television actress")
        db.session.add_all([episode1, episode2, guest1, guest2, guest3])
        db.session.commit()
        appearance1 = Appearance(rating=4, episode_id=episode1.id, guest_id=guest1.id)
        db.session.add(appearance1)
        db.session.commit()

    client = app.test_client()

    # Test GET /episodes
    resp = client.get('/episodes')
    print("GET /episodes:", resp.status_code, resp.get_json())

    # Test GET /episodes/1 (valid)
    resp = client.get('/episodes/1')
    print("GET /episodes/1:", resp.status_code, resp.get_json())

    # Test GET /episodes/999 (invalid)
    resp = client.get('/episodes/999')
    print("GET /episodes/999:", resp.status_code, resp.get_json())

    # Test GET /guests
    resp = client.get('/guests')
    print("GET /guests:", resp.status_code, resp.get_json())

    # Test POST /appearances valid
    resp = client.post('/appearances', json={
        "rating": 5,
        "episode_id": 2,
        "guest_id": 3
    })
    print("POST /appearances valid:", resp.status_code, resp.get_json())

    # Test POST /appearances invalid rating
    resp = client.post('/appearances', json={
        "rating": 6,
        "episode_id": 1,
        "guest_id": 1
    })
    print("POST /appearances invalid rating:", resp.status_code, resp.get_json())

    # Test POST /appearances missing fields
    resp = client.post('/appearances', json={
        "rating": 3
    })
    print("POST /appearances missing fields:", resp.status_code, resp.get_json())

if __name__ == "__main__":
    run_tests()
