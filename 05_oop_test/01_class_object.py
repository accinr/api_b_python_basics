class Book:
    def __init__(self, author, pages, title):
        self.author = author
        self.pages = pages
        self.title = title

    def get_title(self):
        return self.title

author = input("Enter Author name ")
num_pages = int(input("Enter number of pages "))
book_title = input("Enter title of the book ")

cpp = Book(author, num_pages, book_title)
# cpp = Book("Bill",258, "Cpp OOP")
print(f"Author is {cpp.author}")
print(f"Title is {cpp.get_title()}")



        
        
