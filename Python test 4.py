class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
        print(f"You have borrowed '{self.title}' by {self.author}.")  
    def return_book(self):
        self.is_borrowed = False    
        print(f"You have returned '{self.title}' by {self.author}.") 

book1 = Book("The Hobbit", "J.R.R. Toklien")    
book2 = Book("1984", "George Orwel")    
book3 = Book("James and the giant peach", "ROALD DAHL")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()