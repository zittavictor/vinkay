class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"The book '{book.title}' by {book.author} is not found in the library")

    def display_books(self):
        print(f'Books in the library include:')
        if self.books:
            for book in self.books:
                print(f'title: {book.title},author: {book.author}')
        else:
            print('the library is currently empty')


my_library = Library('my library')
book1 = Book('harry potter', 'j.k rowling')
book2 = Book('persy jackson', 'rick  riordan')
book3 = Book('nelson mandela', 'nelson mandela')

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.display_books()
my_library.remove_book(book2)
my_library.display_books()