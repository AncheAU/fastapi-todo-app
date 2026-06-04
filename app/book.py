from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BookCreate(BaseModel):
    title: str
    author: str

class BookUpdate(BaseModel):
    is_read: bool

books = [
     {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert Martin",
        "is_read": False
    },
    {
        "id": 2,
        "title": "Pragmatic Programming",
        "author": "Hunt/Thomas",
        "is_read": False
    },
    {
        "id": 3,
        "title": "Design Pattern",
        "author": "Gamma et al",
        "is_read": False
    },
    {
        "id": 4,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "is_read": False
    }
]


#Home
@app.get("/")
def home():
    return {
        "message": "Book API is running."
    }


#Get all books
@app.get("/books")
def get_all_books():
    return books


#Create a book
@app.post("/books")
def create_book(create_book: BookCreate):
    new_book = {
        "id": max(book["id"] for book in books) + 1,
        "title": create_book.title,
        "author": create_book.author,
        "is_read": False
    }

    books.append(new_book)
    return new_book

#Statistics of the books
@app.get("/books/stats")
def statistics_books():
    read_book = 0
    unread_book = 0

    for book in books:
        if book["is_read"]:
            read_book += 1
        else:
            unread_book += 1
    
    return {
        "total_books": len(books),
        "read": read_book,
        "unread": unread_book
    }

#Get read books only
@app.get("/books/read")
def get_read_books():
    result = []
    for book in books:
        if book["is_read"]:
            result.append(book)
    
    if result != []:
        return{
            "results": result
        }
    else:
        return {
            "error": "No read books."
        }

#Get single one book
@app.get("/books/{book_id}")
def get_single_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
        
    return {
        "error": f"Book with ID {book_id} does not exist."
        }

#Update book is_read to True
@app.put("/books/{book_id}")
def update_book_status(book_id: int, updateBook: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book["is_read"] = updateBook.is_read

            return book
    
    return {
        "error": f"Book with ID {book_id} does not exist."
    }

#Delete book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
        
            return {
                "message": "Book deleted successfully.",
                "deleted": deleted_book
            }
    
    return {
        "error": f"Book with ID {book_id} does not exist."
    }

#Search for book
@app.get("/books/search/{title}")
def search_book(title: str):
    result = []
    for book in books:
        if title.lower() in book["title"].lower():
            result.append(book)
    
    if result == []:
        return {
            "error": "No books found."
        }
    else:
        return {
            "results": result
        }


