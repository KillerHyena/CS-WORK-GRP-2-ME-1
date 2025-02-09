#Implement inheritance by creating subclasses for different types of books
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages   
    def display_info(self):
        print("\nBook Details:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")   
    def is_long_book(self):
        return self.pages > 300
# Subclass for Fiction Books
class FictionBook(Book):
    def __init__(self, title, author, pages, genre, protagonist):
        super().__init__(title, author, pages)
        self.genre = genre
        self.protagonist = protagonist   
    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")
        print(f"Protagonist: {self.protagonist}")
# Subclass for Academic Books
class AcademicBook(Book):
    def __init__(self, title, author, pages, subject, level):
        super().__init__(title, author, pages)
        self.subject = subject
        self.level = level  
    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"Academic Level: {self.level}")
# Subclass for Comic Books
class ComicBook(Book):
    def __init__(self, title, author, pages, illustrator, publisher):
        super().__init__(title, author, pages)
        self.illustrator = illustrator
        self.publisher = publisher  
    def display_info(self):
        super().display_info()
        print(f"Illustrator: {self.illustrator}")
        print(f"Publisher: {self.publisher}")
type_of_book = input("Enter book type (Fiction/Academic/Comic): ").strip().lower()
title = input("Enter book title: ")
author = input("Enter book author: ")
pages = int(input("Enter number of pages: "))
if type_of_book == "fiction":
    genre = input("Enter genre: ")
    protagonist = input("Enter protagonist name: ")
    book = FictionBook(title, author, pages, genre, protagonist)
elif type_of_book == "academic":
    subject = input("Enter subject: ")
    level = input("Enter academic level (Beginner/Intermediate/Advanced): ")
    book = AcademicBook(title, author, pages, subject, level)
elif type_of_book == "comic":
    illustrator = input("Enter illustrator name: ")
    publisher = input("Enter publisher name: ")
    book = ComicBook(title, author, pages, illustrator, publisher)
else:
    book = Book(title, author, pages)
book.display_info()
print("Is long book:", book.is_long_book())