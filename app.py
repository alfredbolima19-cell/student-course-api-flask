
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# CORS for classroom API demonstration
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Fictional course catalogue
courses = [
    {
        "id": 1,
        "code": "CS 101",
        "name": "Introduction to Computing",
        "description": "Learn the basics of computers and information technology."
    },
    {
        "id": 2,
        "code": "IT 204",
        "name": "Web Development",
        "description": "Learn how to create websites and web applications."
    },
    {
        "id": 3,
        "code": "IT 305",
        "name": "Database Management",
        "description": "Learn database concepts and data management."
    },
    {
        "id": 4,
        "code": "CS 202",
        "name": "Programming Fundamentals",
        "description": "Learn basic programming concepts and problem solving."
    },
    {
        "id": 5,
        "code": "IT 310",
        "name": "Systems Integration",
        "description": "Learn how different information systems communicate."
    }
]


# Endpoint 1: API health check
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Student Course API is running"
    }), 200


# Endpoint 2: Get all courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses), 200


# Endpoint 3: Get a course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return jsonify(course), 200

    return jsonify({
        "error": "Course not found"
    }), 404


# Run the application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
