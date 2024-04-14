from typing import List
from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from pydantic import BaseModel

from jose import jwt

app = FastAPI()


# Mock database for notes
notes_db = []

# Pydantic model for Note
class Note(BaseModel):
    id: int
    title: str
    content: str


# JWT settings
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# User model for authentication
class User(BaseModel):
    username: str
    password: str
    disabled: bool
    role: str

# Hardcoded user for demonstration purposes
fake_user = User(username="user", password="password", disabled=False, role="user")

# JWT token helper functions
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Authenticate user and generate JWT token
def authenticate_user(username: str, password: str):
    if username == fake_user.username and password == fake_user.password:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": username, "role": fake_user.role}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Endpoint to generate JWT token
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return authenticate_user(form_data.username, form_data.password)

# CRUD operations for notes with JWT authentication
@app.post("/notes/", response_model=Note)
def create_note(note: Note, token: str = Depends(login)):
    new_note = Note(id=len(notes_db) + 1, title=note.title, content=note.content)
    notes_db.append(new_note)
    return new_note

@app.get("/notes/", response_model=List[Note])
def read_notes(token: str = Depends(login)):
    return notes_db

@app.get("/notes/{note_id}", response_model=Note)
def read_note(note_id: int, token: str = Depends(login)):
    for note in notes_db:
        if note.id == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note: Note, token: str = Depends(login)):
    for idx, db_note in enumerate(notes_db):
        if db_note.id == note_id:
            notes_db[idx] = Note(id=note_id, title=note.title, content=note.content)
            return notes_db[idx]
    raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, token: str = Depends(login)):
    for idx, note in enumerate(notes_db):
        if note.id == note_id:
            del notes_db[idx]
            return {"message": "Note deleted"}
    raise HTTPException(status_code=404, detail="Note not found")
