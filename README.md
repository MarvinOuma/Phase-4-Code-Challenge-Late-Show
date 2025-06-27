# Late Show Flask API

This project is a Flask API for the Late Show domain. It provides endpoints to manage Episodes, Guests, and Appearances with proper relationships, validations, and error handling.

## Features

- Models: Episode, Guest, Appearance with many-to-many relationships
- Validations on Appearance rating (1 to 5)
- Cascade deletes for related appearances
- RESTful API routes:
  - GET /episodes
  - GET /episodes/:id
  - GET /guests
  - POST /appearances
- Proper error handling with JSON responses
- Database migrations with Flask-Migrate
- Seed script to populate database from CSV or generated data
- Thorough testing of all endpoints and edge cases

## Setup Instructions

1. Clone the repository https://github.com/MarvinOuma/Phase-4-Code-Challenge-Late-Show

2. Create and activate a virtual environment (optional but recommended):

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
   flask db migrate
   flask db upgrade
   ```

5. Seed the database:

   ```bash
   python seed.py
   ```

6. Run the Flask app:

   ```bash
   python app.py
   ```

   By default, the app runs on port 5000. If port 5000 is in use, run on a different port:

   ```bash
   python app.py --port 5001
   ```

## Testing

Run the thorough test script to verify all endpoints and edge cases:

```bash
python thorough_test.py
```

## API Endpoints

- `GET /episodes` - List all episodes
- `GET /episodes/:id` - Get episode details with appearances and guest info
- `GET /guests` - List all guests
- `POST /appearances` - Create a new appearance with rating validation

## Notes

- Use the provided Postman collection to test the API endpoints.
- The seed script can be modified to use your own CSV data if needed.

## Author

Marvin Daniel

## License

MIT License
