class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f"{book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"Book '{title}' borrowed successfully.")
                return True
        print(f"Sorry, '{title}' is either not available or does not exist in the library.")
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"Book '{title}' returned successfully.")
                return True
        print(f"Sorry, '{title}' was not borrowed or does not exist in the library.")
        return False

# Example usage
library = Library()

# Adding books to the library
library.add_book("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")
library.add_book("India that is Bharat", "J Sai Deepak")
library.add_book("Five Point Someone", "Chetan Bhagat")
library.add_book("The Shadow Lines", "Amitav Ghosh")
library.add_book("Revolution 2020", "Chetan Bhagat")
library.add_book("Swami and Friends", "R.K. Narayan")
library.add_book("Sea of Poppies", "Amitav Ghosh")
library.add_book("Gitanjali", "Rabindranath Tagore")

# Displaying available books
library.display_books()

# Borrowing a book (soft code)
while True:
    book_to_borrow = input("Enter the title of the book you want to borrow: ")
    if library.borrow_book(book_to_borrow):
        break

# Displaying available books after borrowing
library.display_books()

# Returning a book (soft code)
while True:
    book_to_return = input("Enter the title of the book you want to return: ")
    if library.return_book(book_to_return):
        break

# Displaying available books after returning
library.display_books()