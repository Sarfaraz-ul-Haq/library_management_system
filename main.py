from typing import List


class Book:
    def __init__(self, book_id: int, title: str, author: str) -> None:
        self.book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self.available: bool = True

    def display_info(self) -> None:
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.available}")

    def display_book_id(self) -> None:
        print(self.book_id)

    def display_title(self) -> None:
        print(self.title)

    def display_author(self) -> None:
        print(self.author)

    def display_available(self) -> None:
        print(self.available)


class User:
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id: str = user_id
        self.name: str = name
        self.email: str = email


class Librarian(User):
    def __init__(self, user_id: str, name: str, email: str) -> None:
        super().__init__(user_id, name, email)

    def add_book() -> None:
        pass

    def update_book() -> None:
        pass

    def delete_book() -> None:
        pass


class Member(User):
    def __init__(self, user_id: str, name: str, email: str) -> None:
        super().__init__(user_id, name, email)

    def borrow_book() -> None:
        pass

    def return_book() -> None:
        pass


class LibraryManager:
    def __init__(self) -> None:
        self.books: List[Book] = []
        self.users: List[User] = []
        # self.load_books()
        # self.load_users()

    # def update_book() -> None:
    #     pass

    # def delete_book() -> None:
    #     pass

    # def borrow_book() -> None:
    #     pass

    # def return_book() -> None:
    #     pass

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    book_id, title, author, available = line.strip().split(",")
                    self.books.append(Book(book_id, title, author))
        except OSError:
            print("Error loading book data from file.")


library: LibraryManager = LibraryManager()
print(library.books)
library.load_books()

for book in library.books:
    print(book.display_info())
