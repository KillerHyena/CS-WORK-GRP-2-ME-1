#Create a class to represent a book with attributes and methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages   
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")   
    def is_long_book(self):
        return self.pages > 300
title = input("Enter book title: ")
author = input("Enter book author: ")
pages = int(input("Enter number of pages: "))
book = Book(title, author, pages)
book.display_info()
print("Is long book:", book.is_long_book())
