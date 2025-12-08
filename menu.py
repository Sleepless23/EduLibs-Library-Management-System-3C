from book_management import book_management_menu
from student_management import student_management_menu
from borrow_return import borrow_return_menu, user_borrow_return_menu
from reporting import reporting_menu
from data_manager import get_students, get_books

def main_menu(role, user_id):
    while True:
        print("\n" + "="*50)
        print(f"=== Main Menu (ADMIN) ===")
        print("="*50)
        print("1. Book Management")
        print("2. Student Management")
        print("3. Borrow / Return")
        print("4. Reporting")
        print("5. Logout")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            book_management_menu()
        elif choice == '2':
            student_management_menu()
        elif choice == '3':
            borrow_return_menu()
        elif choice == '4':
            reporting_menu()
        elif choice == '5':
            print("\nLogging out...")
            break
        else:
            print("Invalid choice! Please try again.")

def user_menu(student_id):
    students = get_students()
    student = students[student_id]
    
    while True:
        print("\n" + "="*50)
        print(f"=== Welcome, {student['name']} ===")
        print("="*50)
        print("1. Browse Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. My Borrowed Books")
        print("5. Logout")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            browse_books()
        elif choice == '2':
            user_borrow_book(student_id)
        elif choice == '3':
            user_return_book(student_id)
        elif choice == '4':
            view_my_books(student_id)
        elif choice == '5':
            print("\nLogging out...")
            break
        else:
            print("Invalid choice! Please try again.")

def browse_books():
    print("\n--- Browse Available Books ---")
    books = get_books()
    
    if not books:
        print("No books available in the library!")
        return
    
    print("\n" + "="*80)
    print(f"{'Book ID':<12} {'Title':<35} {'Author':<25} {'Available':<10}")
    print("-"*80)
    
    for book_id, book in books.items():
        print(f"{book_id:<12} {book['title']:<35} {book['author']:<25} {book['available']}/{book['quantity']}")
    
    print("="*80)

def user_borrow_book(student_id):
    from borrow_return import user_borrow_book_process
    user_borrow_book_process(student_id)

def user_return_book(student_id):
    from borrow_return import user_return_book_process
    user_return_book_process(student_id)

def view_my_books(student_id):
    from data_manager import get_borrowed_books, get_books, get_students
    from datetime import datetime
    
    borrowed_books = get_borrowed_books()
    books = get_books()
    students = get_students()
    
    student = students[student_id]
    
    print(f"\n--- My Borrowed Books ---")
    print(f"Student: {student['name']}")
    print("="*80)
    
    has_books = False
    for borrow_id, record in borrowed_books.items():
        if record['student_id'] == student_id and not record['returned']:
            has_books = True
            book = books[record['book_id']]
            
            # Check if overdue
            due_date = datetime.strptime(record['due_date'], "%Y-%m-%d")
            today = datetime.now()
            status = "On Time"
            
            if today > due_date:
                days_overdue = (today - due_date).days
                status = f"⚠ OVERDUE ({days_overdue} days)"
            
            print(f"\nBook: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Borrowed: {record['borrow_date']}")
            print(f"Due Date: {record['due_date']}")
            print(f"Status: {status}")
            print("-"*80)
    
    if not has_books:
        print("You have no borrowed books.")
    
    print("="*80)