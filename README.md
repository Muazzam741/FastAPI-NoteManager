# TaskNote

## Description

The FastAPI Notes App is a simple web application built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
This app allows users to perform CRUD operations (Create, Read, Update, Delete) on notes. Users can add new notes, view existing notes, update notes, and delete notes using secure JWT authentication.

## Features
- Secure JWT authentication for user login
- Create new notes with a title and content
- View existing notes
- Update notes
- Delete notes

## Technologies Used
- FastAPI
- Python
- Pydantic
- JWT (JSON Web Tokens)
- SQLite (for mock database)

## Installation
1. Clone the repository
https://github.com/Muazzam741/FastAPI-NoteManager.git
2. Navigate to the project directory:
`cd fastapi-notes-app`
3. Install dependencies:
`pip install -r requirements.txt`
4. Start the FastAPI server:
`uvicorn main:app --reload`
5. Open your browser and go to http://localhost:8000 to use the app.

## Usage
1. Register or login using the provided credentials.
2. Add new notes, update existing notes, view notes, and delete notes as needed.

## API Endpoints
- POST /token: Generate JWT token for authentication
- POST /notes/: Create a new note
- GET /notes/: Get all notes
- GET /notes/{note_id}: Get a specific note by ID
- PUT /notes/{note_id}: Update a note
- DELETE /notes/{note_id}: Delete a note

For detailed API documentation, visit http://localhost:8000/docs.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgements
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [JWT Documentation](https://jwt.io/introduction)
