class Library:
    def __init__(self):
        self.books = {
            "Python Crash Course": True,
            "Clean Code": True,
            "The Great Gatsby": False,
        }

    def check_availability(self, book_title):
        if book_title in self.books:
            if self.books[book_title]:
                print(f"Yes, '{book_title}' is currently AVAILABLE for borrowing.")
            else:
                print(f"Sorry, '{book_title}' is currently CHECKED OUT.")
        else:
            print(f"We couldn't find '{book_title}' in the library catalog.")

    def view_catalog(self):
        print("\n--- Library Catalog ---")
        for title, available in self.books.items():
            status = "Available" if available else "Checked Out"
            print(f"- {title} [{status}]")

my_library = Library()

while True:
    print("\nWhat would you like to do?")
    print("1. View all books")
    print("2. Check availability of a specific book")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        my_library.view_catalog()
    elif choice == '2':
        book = input("Enter the book title to check: ")
        my_library.check_availability(book)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
