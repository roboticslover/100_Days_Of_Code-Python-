class Library:
    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books

    def is_complete(self):
        return self.no_of_books == self.books


library = Library(100, 700)
is_complete = library.is_complete()
if is_complete:
    print("Complete!!!")
else:
    print("Incomplete!!!")
