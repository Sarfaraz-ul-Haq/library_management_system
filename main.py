from typing import List, Optional


class Book:
    def __init__(
        self, book_id: str, title: str, author: str, available: bool = True
    ) -> None:
        self._book_id: str = book_id
        self._title: str = title
        self._author: str = author
        self._available: bool = available

    def display_info(self) -> None:
        print(f"Book ID: {self._book_id}")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"{'Book is available' if self._available else 'Book is not Available'}")

    @property
    def book_id(self) -> str:
        return self._book_id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = value

    @property
    def available(self) -> bool:
        return self._available

    @available.setter
    def available(self, value: bool) -> None:
        self._available = value


class User:
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self._user_id: str = user_id
        self._name: str = name
        self._email: str = email

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value


class Librarian(User):
    def __init__(self, user_id: str, name: str, email: str) -> None:
        super().__init__(user_id, name, email)

    def add_book(self, book: Book, library_manager: "LibraryManager") -> None:
        library_manager.add_book(book)

    def update_book(
        self,
        library_manager: "LibraryManager",
        book_id: Optional[str],
        title: Optional[str],
        author: Optional[str],
    ) -> None:
        library_manager.update_book(book_id, title, author)

    def delete_book(self, book_id: str, library_manager: "LibraryManager") -> None:
        library_manager.delete_book(book_id)


class Member(User):
    def __init__(self, user_id: str, name: str, email: str) -> None:
        super().__init__(user_id, name, email)
        self._borrowed_books: List[Book] = []

    @property
    def borrowed_books(self) -> List[Book]:
        return self._borrowed_books

    def add_borrowed_book(self, book: Book) -> None:
        self._borrowed_books.append(book)

    def remove_borrowed_book(self, book: Book) -> None:
        self._borrowed_books.remove(book)

    def borrow_book(self, library_manager: "LibraryManager", book_id: str) -> None:
        library_manager.borrow_book(self, book_id)

    def return_book(self, library_manager: "LibraryManager", book_id: str) -> None:
        library_manager.return_book(self, book_id)


class LibraryManager:
    _total_books: int = 0
    _total_users: int = 0

    def __init__(self) -> None:
        self.books: List[Book] = self.load_books()
        self.users: List[User] = self.load_users()
        LibraryManager._total_books = len(self.books)
        LibraryManager._total_users = len(self.users)

    @classmethod
    def get_total_books(cls) -> int:
        return cls._total_books

    @classmethod
    def get_total_users(cls) -> int:
        return cls._total_users

    @classmethod
    def increment_total_books(cls) -> None:
        cls._total_books += 1

    @classmethod
    def decrement_total_books(cls) -> None:
        cls._total_books -= 1

    @classmethod
    def increment_total_users(cls) -> None:
        cls._total_users += 1

    @classmethod
    def decrement_total_users(cls) -> None:
        cls._total_users -= 1

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        LibraryManager.increment_total_books()
        print(f"Book '{book.title}' added successfully.\n")

    def delete_book(self, book_id: str):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                LibraryManager.decrement_total_books()
                print(f"Book ID {book_id} deleted successfully.\n")
                return

    def update_book(self, book_id: str, title: Optional[str], author: Optional[str]):
        for book in self.books:
            if book.book_id == book_id:
                if title:
                    book.title = title
                    print(f"Book title {title} updated successfully.\n")
                if author:
                    book.author = author
                    print(f"Book author {author} updated successfully.\n")
                return
        print(f"Book ID {book_id} not found.\n")

    def borrow_book(self, member: Member, book_id: str):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                member.add_borrowed_book(book)
                print(
                    f"Book '{book.title}' borrowed successfully by member '{member.name}'.\n"
                )
                return
        print(f"Book ID {book_id} is not available.\n")

    def return_book(self, member: Member, book_id: str) -> None:
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    if book in member.borrowed_books:
                        member.remove_borrowed_book(book)
                        print(f"Book '{book.title}' returned successfully.\n")
                    else:
                        print(
                            f"Book '{book.title}' is not borrowed by member '{member.name}'.\n"
                        )
                    return
                else:
                    print(f"Book ID {book_id} is not currently borrowed.\n")
                    return
        print(f"Book ID {book_id} not found.\n")

    def add_user(self, user: User) -> None:
        for existing_user in self.users:
            if existing_user.user_id == user.user_id:
                print(
                    f"User with ID {user.user_id} already exists. Cannot add duplicate.\n"
                )
                return
        self.users.append(user)

        if isinstance(user, Librarian):
            print(f"Librarian '{user.name}' added successfully.\n")
        else:
            print(f"Member '{user.name}' added successfully.\n")

        LibraryManager.increment_total_users()

    def delete_user(self, user_id: str) -> None:
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"User ID {user_id} deleted successfully.\n")
                LibraryManager.decrement_total_users()
                return
        print(f"User ID {user_id} not found.\n")

    def update_user(
        self, user_id: str, name: Optional[str], email: Optional[str]
    ) -> None:
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                if email:
                    user.email = email
                print(f"User ID {user_id} updated successfully.\n")
                return
        print(f"User ID {user_id} not found.\n")

    def save_books(self):
        try:
            with open("books.txt", "w") as file:
                for book in self.books:
                    file.write(
                        f"{book.book_id},{book.title},{book.author},{book.available}\n"
                    )
        except OSError:
            print("Error saving book data to file.\n")

    def load_books(self):
        books: List[Book] = []
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    book_id, title, author, available = line.strip().split(",")
                    if available == "True":
                        available_bool = True
                    else:
                        available_bool = False
                    books.append(Book(book_id, title, author, available_bool))
        except OSError:
            print("Error loading book data from file.\n")

        LibraryManager._total_books = len(books)

        return books

    def save_users(self):
        try:
            with open("users.txt", "w") as file:
                for user in self.users:
                    if isinstance(user, Librarian):
                        file.write(
                            f"{user.user_id},{user.name},{user.email},Librarian\n"
                        )
                    else:
                        file.write(f"{user.user_id},{user.name},{user.email},Member\n")
        except OSError:
            print("Error saving user data to file.\n")

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
            print("Error loading user data from file.\n")

        LibraryManager._total_users = len(users)

        return users

    def save_all_data_to_txt_files(self):
        self.save_books()
        self.save_users()
        print("All changes have been saved successfully to the text files.\n")


library_manager = LibraryManager()


librarian = Librarian("lib001", "Ali", "ali@example.com")
library_manager.add_user(librarian)

member1 = Member("mem001", "Hamzah", "hamzah@example.com")
library_manager.add_user(member1)

member2 = Member("mem002", "Haseeb", "haseeb@example.com")
library_manager.add_user(member2)


book1 = Book("book001", "Nahj ul Balagha", "Ali ibn Abi Talib")
librarian.add_book(book1, library_manager)

book2 = Book("book002", "The Great Gatsby", "F. Scott Fitzgerald")
librarian.add_book(book2, library_manager)


print("Available Books")
for book in library_manager.books:
    book.display_info()

member1.borrow_book(library_manager, "book001")

member2.borrow_book(library_manager, "book001")

member1.return_book(library_manager, "book001")

member2.borrow_book(library_manager, "book001")

library_manager.save_all_data_to_txt_files()
