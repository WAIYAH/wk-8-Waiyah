-- Create the LibraryManagement database
CREATE DATABASE LibraryManagement;
USE LibraryManagement;

-- Table 1: Books (Stores book information)
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY, -- PK, auto-incremented
    Title VARCHAR(255) NOT NULL, -- Book title, required
    Author VARCHAR(100) NOT NULL, -- Author name, required
    ISBN VARCHAR(13) UNIQUE NOT NULL, -- ISBN, unique identifier for books
    PublicationYear INT CHECK (PublicationYear >= 1800), -- Year of publication, constraint for realistic years
    AvailableCopies INT NOT NULL DEFAULT 1 -- Number of available copies, default to 1
);

-- Table 2: Members (Stores member information)
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY, -- PK, auto-incremented
    FirstName VARCHAR(50) NOT NULL, -- First name, required
    LastName VARCHAR(50) NOT NULL, -- Last name, required
    Email VARCHAR(100) UNIQUE NOT NULL, -- Email, unique for each member
    JoinDate DATE NOT NULL -- Date the member joined, required
);

-- Table 3: Transactions (Tracks book borrowing, M-M relationship between Books and Members)
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- PK, auto-incremented
    BookID INT NOT NULL, -- FK to Books
    MemberID INT NOT NULL, -- FK to Members
    BorrowDate DATE NOT NULL, -- Date the book was borrowed
    ReturnDate DATE, -- Date the book was returned (NULL if not returned yet)
    FOREIGN KEY (BookID) REFERENCES Books(BookID) ON DELETE CASCADE, -- FK constraint, cascade delete
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE -- FK constraint, cascade delete
);

-- Insert sample data into Books
INSERT INTO Books (Title, Author, ISBN, PublicationYear, AvailableCopies) VALUES
    ('To Kill a Mockingbird', 'Harper Lee', '9780446310789', 1960, 3),
    ('1984', 'George Orwell', '9780451524935', 1949, 5),
    ('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 2);

-- Insert sample data into Members
INSERT INTO Members (FirstName, LastName, Email, JoinDate) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-01-15'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-03-22'),
    ('Emily', 'Clark', 'emily.clark@example.com', '2023-06-10');

-- Insert sample data into Transactions
INSERT INTO Transactions (BookID, MemberID, BorrowDate, ReturnDate) VALUES
    (1, 1, '2023-07-01', '2023-07-15'), -- John borrowed "To Kill a Mockingbird" and returned it
    (2, 2, '2023-07-05', NULL), -- Jane borrowed "1984" and hasn't returned it
    (3, 3, '2023-07-10', '2023-07-20'); -- Emily borrowed "The Great Gatsby" and returned it
