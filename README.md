# Late Show Flask API

This is a Flask API for the Late Show domain challenge. It manages Episodes, Guests, and Appearances with relationships and validations.

## Setup

1. Clone the repository (private repo named `lateshow-firstname-lastname`).

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run database migrations:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Seed the database:

```bash
python seed.py
```

## Running the App

Start the Flask app:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- `GET /episodes` - List all episodes.
- `GET /episodes/<id>` - Get episode by ID with appearances and guest info.
- `GET /guests` - List all guests.
- `POST /appearances` - Create a new appearance.

### POST /appearances Example Request Body

```json
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 3
}
```

## Testing

Import the provided Postman collection `challenge-4-lateshow.postman_collection.json` to test the API endpoints.

## Notes

- Appearance rating must be between 1 and 5 inclusive.
- Cascade deletes are implemented for appearances when episodes or guests are deleted.
- Proper error handling and status codes are returned.

## License

This project is private and for educational purposes only.
