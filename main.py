from fastapi import FastAPI, HTTPException
from database import get_db_connection
from models import Book

app = FastAPI()

# Create: Add a new book
@app.post("/books/")
def create_book(book: Book):
    connection = get_db_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Books (Title, Author, ISBN, PublicationYear, AvailableCopies)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (book.Title, book.Author, book.ISBN, book.PublicationYear, book.AvailableCopies))
        connection.commit()
        return {"message": "Book added successfully", "BookID": cursor.lastrowid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

# Read: Get all books
@app.get("/books/")
def get_books():
    connection = get_db_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        return books
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

# Read: Get a specific book by BookID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    connection = get_db_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Books WHERE BookID = %s", (book_id,))
        book = cursor.fetchone()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

# Update: Update a book's details
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    connection = get_db_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        cursor = connection.cursor()
        query = """
        UPDATE Books
        SET Title = %s, Author = %s, ISBN = %s, PublicationYear = %s, AvailableCopies = %s
        WHERE BookID = %s
        """
        cursor.execute(query, (book.Title, book.Author, book.ISBN, book.PublicationYear, book.AvailableCopies, book_id))
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"message": "Book updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

# Delete: Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    connection = get_db_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Books WHERE BookID = %s", (book_id,))
        connection.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Book not found")
        return {"message": "Book deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()