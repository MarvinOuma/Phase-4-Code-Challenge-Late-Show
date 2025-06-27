import csv
from app import create_app, db
from models import Episode, Guest, Appearance
import os

app = create_app()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Try to load CSV data
        csv_path = os.path.join(os.path.dirname(__file__), 'lateshow_seed.csv')
        if os.path.exists(csv_path):
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                episodes = {}
                guests = {}
                for row in reader:
                    ep_num = int(row['episode_number'])
                    ep_date = row['episode_date']
                    guest_name = row['guest_name']
                    guest_occupation = row['guest_occupation']
                    rating = int(row['rating'])

                    if ep_num not in episodes:
                        episode = Episode(number=ep_num, date=ep_date)
                        db.session.add(episode)
                        db.session.flush()
                        episodes[ep_num] = episode
                    else:
                        episode = episodes[ep_num]

                    if guest_name not in guests:
                        guest = Guest(name=guest_name, occupation=guest_occupation)
                        db.session.add(guest)
                        db.session.flush()
                        guests[guest_name] = guest
                    else:
                        guest = guests[guest_name]

                    appearance = Appearance(rating=rating, episode_id=episode.id, guest_id=guest.id)
                    db.session.add(appearance)

                db.session.commit()
                print("Database seeded from CSV.")
        else:
            # Fallback seed data
            episode1 = Episode(number=1, date="1/11/99")
            episode2 = Episode(number=2, date="1/12/99")
            guest1 = Guest(name="Michael J. Fox", occupation="actor")
            guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
            guest3 = Guest(name="Tracey Ullman", occupation="television actress")

            db.session.add_all([episode1, episode2, guest1, guest2, guest3])
            db.session.commit()

            appearance1 = Appearance(rating=4, episode_id=episode1.id, guest_id=guest1.id)
            appearance2 = Appearance(rating=5, episode_id=episode2.id, guest_id=guest3.id)

            db.session.add_all([appearance1, appearance2])
            db.session.commit()
            print("Database seeded with fallback data.")

if __name__ == "__main__":
    seed_data()
