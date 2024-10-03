class Book:
    def __init__(self, book_id: int, title: str, author: str) -> None:
        self._book_id: int = book_id
        self.title: str = title
        self.author: str = author
        self._available: bool = True

    def display_info(self) -> None:
        print(f"Book ID: {self._book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self._available}")

    def display_book_id(self) -> None:
        print(self._book_id)

    def display_title(self) -> None:
        print(self.title)

    def display_author(self) -> None:
        print(self.author)

    def display_available(self) -> None:
        print(self._available)


class User:
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self._user_id: str = user_id
        self._name: str = name
        self._email: str = email


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
