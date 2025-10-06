class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def getDetails(self):
        print(f"The author is {self.author}")
        
        if True:
            print("True")

    # creating an object
java = Book("Java Author","Java Book")
java.getDetails()

        
