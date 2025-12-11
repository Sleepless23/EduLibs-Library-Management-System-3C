from data_manager import get_books, save_books

def add_new_book():
    print("\n--- Add New Book ---")
    books = get_books()
    
    book_id = input("Enter Book ID: ")
    
    if book_id in books:
        print("Book ID already exists!")
        return
    
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))
    
    books[book_id] = {
        'title': title,
        'author': author,
        'quantity': quantity,
        'available': quantity
    }
    
    save_books(books)
    print("✓ Book added successfully!")

def edit_book_info():
    print("\n--- Edit Book Info ---")
    books = get_books()
    
    book_id = input("Enter Book ID to edit: ")
    
    if book_id not in books:
        print("Book not found!")
        return
    
    print(f"\nCurrent info:")
    print(f"Title: {books[book_id]['title']}")
    print(f"Author: {books[book_id]['author']}")
    print(f"Quantity: {books[book_id]['quantity']}")
    print("\nLeave blank to keep current value")
    
    title = input("Enter new Title: ")
    author = input("Enter new Author: ")
    quantity = input("Enter new Quantity: ")
    
    if title:
        books[book_id]['title'] = title
    if author:
        books[book_id]['author'] = author
    if quantity:
        new_qty = int(quantity)
        books[book_id]['quantity'] = new_qty
        books[book_id]['available'] = new_qty
    
    save_books(books)
    print("✓ Book info updated!")

def delete_book():
    print("\n--- Delete Book ---")
    books = get_books()
    
    book_id = input("Enter Book ID to delete: ")
    
    if book_id not in books:
        print("Book not found!")
        return
    
    print(f"\nBook to delete: {books[book_id]['title']}")
    confirm = input("Are you sure? (yes/no): ")
    
    if confirm.lower() == 'yes':
        del books[book_id]
        save_books(books)
        print("✓ Book deleted!")
    else:
        print("Deletion cancelled.")

def book_management_menu():
    while True:
        print("\n" + "="*50)
        print("=== Book Management ===")
        print("="*50)
        print("1. Add New Book")
        print("2. Edit Book Info")
        print("3. Delete Book")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            add_new_book()
        elif choice == '2':
            edit_book_info()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            break
        else:
            print("Invalid choice!!")