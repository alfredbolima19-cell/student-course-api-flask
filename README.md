
# Student Course API

A beginner-friendly REST API built with Python and Flask for System Integration and Architecture - Lesson 3.

## Technologies
- Python
- Flask
- Flask-CORS
- Gunicorn
- GitHub
- Render

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/health | Check API status |
| GET | /api/courses | Retrieve all courses |
| GET | /api/courses/1 | Retrieve a course by ID |

## Sample Course Data

The API contains five fictional courses:
- CS 101 - Introduction to Computing
- IT 204 - Web Development
- IT 305 - Database Management
- CS 202 - Programming Fundamentals
- IT 310 - Systems Integration

## Error Handling

Requesting an unavailable course ID returns HTTP 404 with a JSON error message.

## Run Locally

1. Install Python.
2. Install dependencies:

   pip install -r requirements.txt

3. Start the application:

   python app.py

4. Open http://localhost:5000/api/health

## Testing

Test these four endpoints:

1. GET /api/health - Expected HTTP 200.
2. GET /api/courses - Expected HTTP 200 and at least five courses.
3. GET /api/courses/1 - Expected HTTP 200.
4. GET /api/courses/9999 - Expected HTTP 404.

## Render Deployment

Build command:

pip install -r requirements.txt

Start command:

gunicorn app:app

Runtime: Python 3

## Project Limitations

- Uses fictional sample data only.
- Does not use a database.
- Does not include authentication.
- Read-only API; no create, update, or delete operations.
- Intended for learning and demonstration, not production use.
