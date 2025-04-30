# Library Management System API

## Project Title
Library Management System with CRUD API

## Description
This project implements a Library Management System with a MySQL database and a CRUD API for managing books. It includes:
- A MySQL database with three tables: `Books`, `Members`, and `Transactions`.
- A FastAPI-based API to perform CRUD operations (Create, Read, Update, Delete) on the `Books` table.
- Relationships between tables: Members borrow books (many-to-many via Transactions).

## How to Run/Set Up the Project
1. **Set Up MySQL Database**:
   - Install MySQL and MySQL Workbench.
   - Run the `library_db.sql` script to create the `LibraryManagement` database and tables with sample data.

2. **Set Up the API**:
   - Ensure Python 3.8+ is installed.
   - Clone this repository:
     ```bash
     git clone <repository-url>
     cd library-api
     ```
   - Install dependencies:
     ```bash
     pip install fastapi uvicorn mysql-connector-python pydantic
     ```
   - Update the database connection in `database.py` with your MySQL credentials (username and password).
   - Run the FastAPI application:
     ```bash
     uvicorn main:app --reload
     ```
   - Access the API at `http://127.0.0.1:8000` and use the Swagger UI at `http://127.0.0.1:8000/docs` to test the endpoints.

3. **API Endpoints**:
   - `POST /books/`: Create a new book.
   - `GET /books/`: Get all books.
   - `GET /books/{book_id}`: Get a specific book by ID.
   - `PUT /books/{book_id}`: Update a book.
   - `DELETE /books/{book_id}`: Delete a book.

## Screenshot or Link to ERD
- **ERD**: The Entity-Relationship Diagram is available at img/erd.png.

## SQL Script
The `library_db.sql` file contains the database schema and sample data.
