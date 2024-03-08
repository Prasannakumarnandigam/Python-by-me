class Book:
    def __init__(self, title, author, price):
        self.title= title
        self.author = author
        self.price =price

    def show_details(self):
        print(self.title)
        print(self.author)
        print(self.price)

book1 = Book("Rich dad and Poor Dad", "Robert", 300)

print(book1.show_details())