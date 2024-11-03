from typing import List, Optional


class Book:
    total_books: int = 0

    def __init__(self, book_id: int, title: str, author: str) -> None:
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.available: bool = True
        Book.total_books += 1

    def display_info(self) -> None:
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.available}\n")

    def display_book_id(self) -> None:
        print(self.book_id)

    def display_title(self) -> None:
        print(self.title)

    def display_author(self) -> None:
        print(self.author)

    def display_available(self) -> None:
        print(self.available)

    @classmethod
    def get_total_books(cls):
        print(cls.total_books)


class User:
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id: str = user_id
        self.name: str = name
        self.email: str = email


class Librarian(User):
    def __init__(self, user_id: str, name: str, email: str) -> None:
        super().__init__(user_id, name, email)

    def add_book(self, book: Book, library_manager) -> None:
        library_manager.add_book(book)

    def update_book(
        self,
        library_manager: "LibraryManager",
        book_id: Optional[int],
        title: Optional[str],
        author: Optional[str],
    ) -> None:
        library_manager.update_book(book_id, title, author)

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
        self.books: List[Book] = self.load_books()
        self.users: List[User] = self.load_users()

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def update_book(self, book_id: int, title: Optional[str], author: Optional[str]):
        for book in self.books:
            if book.book_id == book_id:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_books()
                print(f"Book ID {book_id} updated successfully.")
                return
        print(f"Book ID {book_id} not found.")

    # def update_book() -> None:
    #     pass

    # def delete_book() -> None:
    #     pass

    # def borrow_book() -> None:
    #     pass

    # def return_book() -> None:
    #     pass

    def save_books(self):
        try:
            with open("books.txt", "w") as file:
                for book in self.books:
                    file.write(
                        f"{book.book_id},{book.title},{book.author},{book.available}"
                    )
        except OSError:
            print("Error saving book data to file.")

    def load_books(self):
        books: List[Book] = []
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    book_id, title, author, available = line.strip().split(",")
                    books.append(Book(book_id, title, author))
        except OSError:
            print("Error loading book data from file.")
        return books

    def save_users(self):
        try:
            with open("users.txt", "w") as file:
                for user in self.users:
                    if isinstance(user, Librarian):
                        file.write(f"{user.user_id},{user.name},{user.email},Librarian")
                    else:
                        file.write(f"{user.user_id},{user.name},{user.email},Member")
        except OSError:
            print("Error saving user data to file.")

    def load_users(self):
        users: List[User] = []
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    user_id, name, email, user_type = line.strip().split(",")
                    if user_type == "Librarian":
                        users.append(Librarian(user_id, name, email))
                    elif user_type == "Member":
                        users.append(Member(user_id, name, email))
        except OSError:
            print("Error loading user data from file.")

        return users


library: LibraryManager = LibraryManager()
# print(library.books)
# library.load_books()

for book in library.books:
    book.display_info()
