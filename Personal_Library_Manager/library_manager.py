import json
import os

LIBRARY_FILE = "library.txt"
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE,"r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE,"w") as file:
        json.dump(library,file)
    
def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    library.append({
        "title":title,
        "author":author,
        "year":year,
        "genre":genre,
        "read":read
    })
    save_library(library)
    print(f"Book '{title}' added successfully.")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print(f"Book '{title}' removed successfully.")
            return
    print(f"Book '{title}' not found in the library.")

def search_book(library):
    print("""Search By:
          1. Title
          2. Author""")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title to search for: ")
        for book in library:
            if book["title"].lower() == title.lower():
                print(f"Matching Books:\n{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {'Read' if book["read"] else 'Not Read'}")
                return
            print(f"No books found with title '{title}'.")
    elif choice == "2":
        author = input("Enter the author to search for: ")
        for book in library:
            if book["author"].lower() == author.lower():
                print(f"Matching Books:\n{book}")
                return
            print(f"No books found with author '{author}'.")
    else:
        print("Invalid choice. Please try again.")

def display_statistics(library):
    read_count = 0
    total_books = len(library)
    if total_books == 0:
        print("The library is empty.")
        return
    
    for book in library:
        if book["read"]:
            read_count += 1
    
    print(f"Total Books: {total_books}")
    print(f"Percentage read: {read_count/total_books * 100}%")

     
def display_library(library):
    for book in library:
        
        print("Your Library:")
        print(f"{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {'Read' if book["read"] else 'Not Read'}")
    
def main():
    library = load_library()
    while True:
        print("Personal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            add_book(library)
        elif user_choice == 2:
            remove_book(library)
        elif user_choice == 3:
            search_book(library)
        elif user_choice == 4:
            library 
        elif user_choice == 5:
            display_statistics(library)
        elif user_choice == 6:
            print("Library saved to file.Good Bye")
        
        else:
            print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    main()


