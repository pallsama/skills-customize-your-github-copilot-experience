# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, fast REST APIs using the FastAPI framework in Python. You will create endpoints to manage a collection of books, implementing common CRUD (Create, Read, Update, Delete) operations.

## 📝 Tasks

### 🛠️	Set Up Your FastAPI Project

#### Description
Initialize a new FastAPI application and create the basic structure needed to run your API server.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a main application file that initializes a FastAPI app instance
- Successfully run the development server on `http://localhost:8000`
- Display the automatic API documentation at `/docs`


### 🛠️	Create Book Endpoints

#### Description
Implement REST API endpoints to manage a collection of books. Each book should have an id, title, author, and year published.

#### Requirements
Completed program should:

- Define a `Book` model using Pydantic with appropriate data types
- Implement `GET /books` to retrieve all books
- Implement `GET /books/{book_id}` to retrieve a single book by ID
- Implement `POST /books` to add a new book
- Implement `PUT /books/{book_id}` to update an existing book
- Implement `DELETE /books/{book_id}` to remove a book
- Return appropriate HTTP status codes (200, 201, 404) for each operation

Example request to create a book:
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925
}
```

Example response:
```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925
}
```


### 🛠️	Add Input Validation

#### Description
Enhance your API with proper input validation to ensure data integrity and provide helpful error messages.

#### Requirements
Completed program should:

- Validate that book titles are between 1 and 100 characters
- Validate that the publication year is between 1000 and the current year
- Return clear error messages when validation fails
- Use Pydantic's built-in validation features
