class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def book_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."
    def read(self):
        return f"Reading '{self.title}'..."
class Fiction(Book):
    def __init__(self, title, author, pages, genre):
        super().__init__(title, author, pages)
        self.genre = genre
    def book_info(self):
        return super().book_info() + f" Genre: {self.genre} (Fiction)."
class NonFiction(Book):
    def __init__(self, title, author, pages, subject):
        super().__init__(title, author, pages)
        self.subject = subject
    def book_info(self):
        return super().book_info() + f" Subject: {self.subject} (Non-Fiction)."
class ScienceFiction(Fiction):
    def __init__(self, title, author, pages, subgenre):
        super().__init__(title, author, pages, "Science Fiction")
        self.subgenre = subgenre
    def book_info(self):
        return super().book_info() + f" Subgenre: {self.subgenre}."
fiction_book = Fiction("The Great Gatsby", "F. Scott Fitzgerald", 180, "Drama")
nonfiction_book = NonFiction("Sapiens", "Yuval Noah Harari", 443, "History")
scifi_book = ScienceFiction("Dune", "Frank Herbert", 412, "Space Opera")
print(fiction_book.book_info())
print(nonfiction_book.book_info())
print(scifi_book.book_info())
print(fiction_book.read())
print(nonfiction_book.read())
print(scifi_book.read())