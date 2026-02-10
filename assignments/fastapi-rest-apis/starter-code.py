"""
FastAPI REST API Assignment - Starter Code
Build a REST API to manage a collection of books.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Initialize FastAPI app
app = FastAPI(
    title="Book Collection API",
    description="A simple REST API to manage books",
    version="1.0.0"
)

# TODO: Define your Book model here using Pydantic
# The model should include: id, title, author, and year


# In-memory storage for books (replace with a database in production)
books = []
next_id = 1


# TODO: Implement GET /books endpoint
# Should return all books in the collection


# TODO: Implement GET /books/{book_id} endpoint
# Should return a single book by ID or 404 if not found


# TODO: Implement POST /books endpoint
# Should create a new book and return it with status 201


# TODO: Implement PUT /books/{book_id} endpoint
# Should update an existing book or return 404 if not found


# TODO: Implement DELETE /books/{book_id} endpoint
# Should delete a book or return 404 if not found


# Run with: uvicorn starter-code:app --reload
