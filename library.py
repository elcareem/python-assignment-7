"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(book, **kwargs):
    """Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
    """
    lib_book = None

    if library:
        lib_book = {"id": len(library) + 1, "title": book, "available": True}
    else:
        lib_book = {"id": 1, "title": book, "available": True}
    
    for item, value in kwargs.items():
        lib_book.update({item: value})
    library.append(lib_book)

    return f"Book {book} added successfully!"


def search_books(**search_param):
    """Search for books by multiple keywords (title, author).
    return books that match search description.
    """
    found = []
    parameters = []
    for param in search_param.items():
        parameters.append(param)

    for book in library:
            if set(parameters).issubset(set(book.items())):
                    found.append(book)
    return found              
    


def borrow_book(book_id):
    """Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
    """
    found = False
    for book in library:
        if book_id == book["id"]:
            found = True
            if book["available"]:
                book["available"] = False
                return f"You borrowed {book["title"]}"
            else:
                return f"Book {book["title"]} not available"
                
    if not found:
        return "Book not found"


add_book("Outliers", author="Mark", genre= "lifestyle")
add_book("Richest Man in Babylon", author="John")
add_book("Outliers 2", author="John", available = False)
add_book("Outliers 3", author="Jane", available = False)


search_books(title = "Outliers", author = "John")

print(borrow_book(5))


