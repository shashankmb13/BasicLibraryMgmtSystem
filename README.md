# 📚 Library Management System (Python)

A simple command-line based **Library Management System** written in Python. It allows users to **add**, **borrow**, **return**, and **view** available books in the library.

## 🚀 Features

- Add new books to the library
- Display all available books
- Borrow a book (mark it as unavailable)
- Return a borrowed book (mark it as available again)
- Case-insensitive book title matching

## 🛠️ Technologies Used

- **Python 3.x**

## 📂 Project Structure


## 📌 How It Works

1. Books are added using the `add_book()` function.
2. Users can borrow and return books by entering titles.
3. The system keeps track of book availability.

## 🧑‍💻 Example Interaction

```text
Available Books:
Harry Potter and the Philosopher's Stone by J.K. Rowling
1984 by George Orwell
...

Enter the title of the book you want to borrow: 1984
Book '1984' borrowed successfully.

Available Books:
Harry Potter and the Philosopher's Stone by J.K. Rowling
...

Enter the title of the book you want to return: 1984
Book '1984' returned successfully.
