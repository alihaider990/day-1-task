class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Added: {book}')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Removed: {book}')
                return
       

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library books:")
            for book in self.books:
                print(book)


library = Library()

book1 = Book("art of everything", "harryporter", 2018)      
book2 = Book("how to make money", "changez", 2008)   

library.add_book(book1)
library.add_book(book2)
library.show_books()
library.remove_book("art of everything")  
library.show_books()
      
     