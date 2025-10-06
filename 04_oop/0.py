class Book:
    def _init_(self, author, title):
        self.author = author
        self.title =title

    def getDetails(self):
        print(f"The author is {self.author}")
        if True:
            print("True")



# creating an object 
java = Book("Java Author", "Java title")
java.getDetails

          
