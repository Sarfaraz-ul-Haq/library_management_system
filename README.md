# Library Management System

## Description

This is a simple **Library Management System** built in Python using Object-Oriented Programming (OOP). The system allows librarians to manage books and users, and members to borrow and return books. Data is stored persistently in text files.

## Classes

### 1. Book

Represents a book in the library.

- **Attributes:**

  - `book_id` (str): Unique identifier for the book.
  - `title` (str): Title of the book.
  - `author` (str): Author of the book.
  - `available` (bool): Indicates if the book is available for borrowing.

- **Methods:**
  - `display_info()`: Displays the book's information.
  - **Property Methods:**
    - `book_id`: Getter for the book ID.
    - `title`: Getter and setter for the book title.
    - `author`: Getter and setter for the book author.
    - `available`: Getter and setter for the book's availability status.

### 2. User

Represents a user of the library system.

- **Attributes:**
  - `user_id` (str): Unique identifier for the user.
  - `name` (str): Name of the user.
  - `email` (str): Email address of the user.

### 3. Librarian (inherits from User)

Represents a librarian with capabilities to manage books and users through the `LibraryManager`.

- **Methods:**
  - `add_book(book, library_manager)`: Adds a new book to the library.
  - `update_book(library_manager, book_id, title, author)`: Updates details of an existing book.
  - `delete_book(book_id, library_manager)`: Removes a book from the library.

### 4. Member (inherits from User)

Represents a library member who can borrow and return books.

- **Attributes:**

  - `_borrowed_books` (List[Book]): List of books currently borrowed by the member.

- **Methods:**
  - `add_borrowed_book(book)`: Adds a book to the member's borrowed list.
  - `remove_borrowed_book(book)`: Removes a book from the member's borrowed list.
  - `borrow_book(library_manager, book_id)`: Borrows a book from the library.
  - `return_book(library_manager, book_id)`: Returns a borrowed book to the library.

### 5. LibraryManager

Manages the library's collection of books and users. Most of the system's functionality resides in this class.

- **Class Attributes:**

  - `_total_books` (int): Total number of books in the library.
  - `_total_users` (int): Total number of users in the library.

- **Attributes:**

  - `books` (List[Book]): List of all books in the library.
  - `users` (List[User]): List of all users (librarians and members) in the library.

- **Methods:**
  - **Book Management:**
    - `add_book(book)`: Adds a new book to the library.
    - `delete_book(book_id)`: Deletes a book from the library by its ID.
    - `update_book(book_id, title, author)`: Updates the title and/or author of a book.
  - **User Management:**
    - `add_user(user)`: Adds a new user (Librarian or Member) to the library.
    - `delete_user(user_id)`: Deletes a user from the library by their ID.
    - `update_user(user_id, name, email)`: Updates a user's name and/or email.
  - **Borrowing Management:**
    - `borrow_book(member, book_id)`: Processes borrowing a book for a member.
    - `return_book(member, book_id)`: Processes returning a book from a member.
  - **Data Persistence:**
    - `save_books()`: Saves all books to `books.txt`.
    - `load_books()`: Loads books from `books.txt`.
    - `save_users()`: Saves all users to `users.txt`.
    - `load_users()`: Loads users from `users.txt`.
    - `save_all_data_to_txt_files()`: Saves all data to both `books.txt` and `users.txt`.
  - **Utility Methods:**
    - `get_total_books()`: Returns the total number of books.
    - `get_total_users()`: Returns the total number of users.
    - `increment_total_books()`: Increments the total book count.
    - `decrement_total_books()`: Decrements the total book count.
    - `increment_total_users()`: Increments the total user count.
    - `decrement_total_users()`: Decrements the total user count.

## Data Files

- **books.txt**: Stores information about all books in the library. Each line contains a book's ID, title, author, and availability status, separated by commas.
- **users.txt**: Stores information about all users in the library. Each line contains a user's ID, name, email, and user type (Librarian or Member), separated by commas.

## Usage

1. **Initialize Library Manager:**

   ```python
   library_manager = LibraryManager()
   ```

2. **Add Users:**

   ```python
   librarian = Librarian("lib001", "Ali", "ali@example.com")
   library_manager.add_user(librarian)

   member1 = Member("mem001", "Hamzah", "hamzah@example.com")
   library_manager.add_user(member1)

   member2 = Member("mem002", "Haseeb", "haseeb@example.com")
   library_manager.add_user(member2)
   ```

3. **Add Books:**

   ```python
   book1 = Book("book001", "Nahj ul Balagha", "Ali ibn Abi Talib")
   librarian.add_book(book1, library_manager)

   book2 = Book("book002", "The Great Gatsby", "F. Scott Fitzgerald")
   librarian.add_book(book2, library_manager)
   ```

4. **Display Available Books:**

   ```python
   print("Available Books")
   for book in library_manager.books:
       book.display_info()
   ```

5. **Borrow and Return Books:**

   ```python
   member1.borrow_book(library_manager, "book001")
   member2.borrow_book(library_manager, "book001")
   member1.return_book(library_manager, "book001")
   member2.borrow_book(library_manager, "book001")
   ```

6. **Save Data:**
   ```python
   library_manager.save_all_data_to_txt_files()
   ```
