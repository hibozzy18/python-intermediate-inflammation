class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return self.title + " by " + self.author
    
    def __eq__(self,  other) -> bool:
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self):
        self.list_of_books = []

    def __len__(self):
        return len(self.list_of_books)
    
    def __getitem__(self, index):
        return self.list_of_books[index]

    def add_book(self, book_title, book_author):

        self.list_of_books.append(Book(book_title, book_author))


    def by_author(self, book_author):

        result_list = []

        for book in self.list_of_books:
            if book.author == book_author:
                result_list.append(book)
        
        if len(result_list) == 0:
            raise KeyError("Author does not exist")
        return result_list

    @property 
    def titles(self):
        
        return [book.title for book in self.list_of_books]
    
    @property
    def authors(self):
        return set([book.author for book in self.list_of_books])

    
    def union(self, other):
        unique_combined = set(self.list_of_books + other.list_of_books)
        library = Library()
        library.list_of_books = list(unique_combined)
        return library

#### 
#Run some tests 
####

library = Library()

library.add_book('My First Book', 'Alice')
library.add_book('My Second Book', 'Alice')
library.add_book('A Different Book', 'Bob')

print(len(library))

book = library[2]
print(book)

books = library.by_author('Alice')
for book in books:
    print(book)

print(library.titles)
print(library.authors)


books = library.by_author('Carol')




        