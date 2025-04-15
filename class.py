# Base class: Book
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    # Method to describe the book
    def describe(self):
        return f"'{self.title}' by {self.author} is a {self.genre} book with {self.pages} pages."

    # Method to read the book
    def read(self):
        return f"You start reading '{self.title}'."


class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size):
        super().__init__(title, author, genre, pages)
        self.__file_size = file_size  

    
    def describe(self):
        return f"'{self.title}' by {self.author} is a {self.genre} eBook with {self.pages} pages and a file size of {self.__file_size} MB."

    
    def get_file_size(self):
        return self.__file_size

    
    def set_file_size(self, size):
        self.__file_size = size


class AudioBook(Book):
    def __init__(self, title, author, genre, pages, duration):
        super().__init__(title, author, genre, pages)
        self.duration = duration  # in hours

    
    def describe(self):
        return f"'{self.title}' by {self.author} is a {self.genre} audiobook with a duration of {self.duration} hours."

    
    def listen(self):
        return f"You start listening to '{self.title}'."

# Example usage:
# Creating book objects
book1 = Book("Pride and Prejudice", "Jane Austen", "Classic Fiction", 281)
ebook1 = EBook("Diary Of A CEO", "Steven Bartlett", "Financial Literacy", 328, 2.5)
audiobook1 = AudioBook("Becoming", "Michelle Obama", "Biography", 426, 19)

# Displaying descriptions and actions
print(book1.describe())
print(book1.read())

print(ebook1.describe())
print(ebook1.get_file_size())
ebook1.set_file_size(3.0)
print(f"Updated file size: {ebook1.get_file_size()}")

print(audiobook1.describe())
print(audiobook1.listen())
