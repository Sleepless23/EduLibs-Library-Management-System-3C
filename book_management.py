from data_manager import get_books, save_books

def add_new_book():
    print("\n--- Add New Book ---")
    books = get_books()
    
    book_id = input("Enter Book ID (or 'cancel' to go back): ")
    if book_id.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    if book_id in books:
        print("Book ID already exists!")
        return
    
    title = input("Enter Book Title (or 'cancel' to go back): ")
    if title.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    author = input("Enter Author (or 'cancel' to go back): ")
    if author.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    quantity = input("Enter Quantity (or 'cancel' to go back): ")
    if quantity.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    quantity = int(quantity)
    
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
    
    book_id = input("Enter Book ID to edit (or 'cancel' to go back): ")
    if book_id.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    if book_id not in books:
        print("Book not found!")
        return
    
    print(f"\nCurrent info:")
    print(f"Title: {books[book_id]['title']}")
    print(f"Author: {books[book_id]['author']}")
    print(f"Quantity: {books[book_id]['quantity']}")
    print("\nLeave blank to keep current value or type 'cancel' to abort")
    
    title = input("Enter new Title: ")
    if title.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    author = input("Enter new Author: ")
    if author.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    quantity = input("Enter new Quantity: ")
    if quantity.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
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
    
    book_id = input("Enter Book ID to delete (or 'cancel' to go back): ")
    if book_id.lower() == 'cancel':
        print("Operation cancelled.")
        return
    
    if book_id not in books:
        print("Book not found!")
        return
    
    print(f"\nBook to delete: {books[book_id]['title']}")
    confirm = input("Are you sure? (yes/no/cancel): ")
    
    if confirm.lower() == 'cancel' or confirm.lower() == 'no':
        print("Deletion cancelled.")
        return
    
    if confirm.lower() == 'yes':
        del books[book_id]
        save_books(books)
        print("✓ Book deleted!")

def display_books():
    print("\n--- Current Books in Library ---")
    books = get_books()

    if not books:
        print("No books found!")
        return

    print("\n" + "="*80)
    print(f"{'Book ID':<12} {'Title':<35} {'Author':<25} {'Available':<10}")
    print("-"*80)

    for book_id, book in books.items():
        print(f"{book_id:<12} {book['title']:<35} {book['author']:<25} {book['available']}/{book['quantity']}")

    print("="*80)

def book_management_menu():
    while True:
        display_books()
        
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
