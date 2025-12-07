from datetime import datetime, timedelta
from data_manager import get_books, save_books, get_students, save_students
from data_manager import get_borrowed_books, save_borrowed_books

def check_availability():
    print("\n--- Check Book Availability ---")
    books = get_books()
    
    book_id = input("Enter Book ID: ")
    
    if book_id in books:
        book = books[book_id]
        print("\n" + "-"*40)
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Total Copies: {book['quantity']}")
        print(f"Available: {book['available']}")
        print(f"Borrowed: {book['quantity'] - book['available']}")
        print("-"*40)
    else:
        print("Book not found!")

def borrow_book():
    print("\n--- Borrow Book (Admin) ---")
    
    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")
    
    students = get_students()
    books = get_books()
    borrowed_books = get_borrowed_books()
    
    
    if student_id not in students:
        print("✗ Student not found!")
        return
    

    if book_id not in books:
        print("✗ Book not found!")
        return
    
    
    if books[book_id]['available'] <= 0:
        print("✗ Book not available!")
        return
    
    
    borrow_date = datetime.now()
    due_date = borrow_date + timedelta(days=14)
    borrow_id = f"{student_id}_{book_id}_{borrow_date.strftime('%Y%m%d%H%M%S')}"
    
    borrowed_books[borrow_id] = {
        'student_id': student_id,
        'book_id': book_id,
        'borrow_date': borrow_date.strftime("%Y-%m-%d"),
        'due_date': due_date.strftime("%Y-%m-%d"),
        'returned': False,
        'overdue': False
    }
    
    
    books[book_id]['available'] -= 1
    students[student_id]['books_borrowed'].append(borrow_id)
    
    save_books(books)
    save_students(students)
    save_borrowed_books(borrowed_books)
    
    print("\n" + "="*40)
    print("✓ Book issued successfully!")
    print(f"Student: {students[student_id]['name']}")
    print(f"Book: {books[book_id]['title']}")
    print(f"Borrow Date: {borrow_date.strftime('%Y-%m-%d')}")
    print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")
    print("="*40)

def user_borrow_book_process(student_id):
    print("\n--- Borrow Book ---")
    
    book_id = input("Enter Book ID: ")
    
    students = get_students()
    books = get_books()
    borrowed_books = get_borrowed_books()
    
    
    if book_id not in books:
        print("✗ Book not found!")
        return
    
    
    if books[book_id]['available'] <= 0:
        print("✗ Book not available!")
        return
    
    
    borrow_date = datetime.now()
    due_date = borrow_date + timedelta(days=14)
    borrow_id = f"{student_id}_{book_id}_{borrow_date.strftime('%Y%m%d%H%M%S')}"
    
    borrowed_books[borrow_id] = {
        'student_id': student_id,
        'book_id': book_id,
        'borrow_date': borrow_date.strftime("%Y-%m-%d"),
        'due_date': due_date.strftime("%Y-%m-%d"),
        'returned': False,
        'overdue': False
    }
    
    
    books[book_id]['available'] -= 1
    students[student_id]['books_borrowed'].append(borrow_id)
    
    save_books(books)
    save_students(students)
    save_borrowed_books(borrowed_books)
    
    print("\n" + "="*40)
    print("✓ Book borrowed successfully!")
    print(f"Book: {books[book_id]['title']}")
    print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")
    print("="*40)

def return_book():
    print("\n--- Return Book (Admin) ---")
    
    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")
    
    students = get_students()
    books = get_books()
    borrowed_books = get_borrowed_books()
    
    
    borrow_id = None
    for bid, record in borrowed_books.items():
        if (record['student_id'] == student_id and 
            record['book_id'] == book_id and 
            not record['returned']):
            borrow_id = bid
            break
    
    if not borrow_id:
        print("✗ No active borrow record found!")
        return
    
    
    return_date = datetime.now()
    borrowed_books[borrow_id]['returned'] = True
    borrowed_books[borrow_id]['return_date'] = return_date.strftime("%Y-%m-%d")
    

    books[book_id]['available'] += 1
    students[student_id]['books_borrowed'].remove(borrow_id)
    
    save_books(books)
    save_students(students)
    save_borrowed_books(borrowed_books)
    
    print("\n✓ Book returned successfully!")
    print(f"Return Date: {return_date.strftime('%Y-%m-%d')}")

def user_return_book_process(student_id):
    print("\n--- Return Book ---")
    
    book_id = input("Enter Book ID to return: ")
    
    students = get_students()
    books = get_books()
    borrowed_books = get_borrowed_books()
    
    
    borrow_id = None
    for bid, record in borrowed_books.items():
        if (record['student_id'] == student_id and 
            record['book_id'] == book_id and 
            not record['returned']):
            borrow_id = bid
            break
    
    if not borrow_id:
        print("✗ You haven't borrowed this book!")
        return
    
    
    return_date = datetime.now()
    borrowed_books[borrow_id]['returned'] = True
    borrowed_books[borrow_id]['return_date'] = return_date.strftime("%Y-%m-%d")
    
    
    books[book_id]['available'] += 1
    students[student_id]['books_borrowed'].remove(borrow_id)
    
    save_books(books)
    save_students(students)
    save_borrowed_books(borrowed_books)
    
    print("\n✓ Book returned successfully!")
    print(f"Thank you for returning '{books[book_id]['title']}'")

def check_overdue():
    print("\n--- Check Overdue Books ---")
    
    borrowed_books = get_borrowed_books()
    students = get_students()
    books = get_books()
    today = datetime.now()
    overdue_found = False
    
    print("\n" + "="*60)
    for borrow_id, record in borrowed_books.items():
        if not record['returned']:
            due_date = datetime.strptime(record['due_date'], "%Y-%m-%d")
            if today > due_date:
                record['overdue'] = True
                overdue_found = True
                
                student_name = students[record['student_id']]['name']
                book_title = books[record['book_id']]['title']
                days_overdue = (today - due_date).days
                
                print(f"\nStudent: {student_name}")
                print(f"Book: {book_title}")
                print(f"Due Date: {record['due_date']}")
                print(f"Days Overdue: {days_overdue}")
                print("-"*60)
    
    if not overdue_found:
        print("No overdue books found!")
    
    print("="*60)
    save_borrowed_books(borrowed_books)

def flag_as_overdue():
    print("\n--- Flag Book as Overdue ---")
    
    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")
    
    borrowed_books = get_borrowed_books()
    
    
    for bid, record in borrowed_books.items():
        if (record['student_id'] == student_id and 
            record['book_id'] == book_id and 
            not record['returned']):
            record['overdue'] = True
            save_borrowed_books(borrowed_books)
            print("✓ Book flagged as overdue!")
            return
    
    print("✗ No active borrow record found!")

def borrow_return_menu():
    while True:
        print("\n" + "="*50)
        print("=== Borrow / Return (Admin) ===")
        print("="*50)
        print("1. Borrow Book for Student")
        print("2. Check Availability")
        print("3. Return Book")
        print("4. Check Overdue")
        print("5. Flag as Overdue")
        print("6. Back to Main Menu")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            borrow_book()
        elif choice == '2':
            check_availability()
        elif choice == '3':
            return_book()
        elif choice == '4':
            check_overdue()
        elif choice == '5':
            flag_as_overdue()
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

def user_borrow_return_menu(student_id):
    while True:
        print("\n" + "="*50)
        print("=== Borrow / Return ===")
        print("="*50)
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Back to Main Menu")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            user_borrow_book_process(student_id)
        elif choice == '2':
            user_return_book_process(student_id)
        elif choice == '3':
            break
        else:
            print("Invalid choice!")