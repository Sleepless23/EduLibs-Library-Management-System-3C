from datetime import datetime
from data_manager import get_books, get_students, get_borrowed_books

def most_borrowed_books():
    print("\n--- Most Borrowed Books Report ---")
    
    borrowed_books = get_borrowed_books()
    books = get_books()
    
    borrow_count = {}
    for record in borrowed_books.values():
        book_id = record['book_id']
        if book_id in borrow_count:
            borrow_count[book_id] += 1
        else:
            borrow_count[book_id] = 1
    
    # Sort by count
    sorted_books = sorted(borrow_count.items(), key=lambda x: x[1], reverse=True)
    
    print("\n" + "="*60)
    print(f"{'Rank':<6} {'Book Title':<35} {'Times Borrowed':<15}")
    print("-"*60)
    
    for i, (book_id, count) in enumerate(sorted_books[:10], 1):
        if book_id in books:
            title = books[book_id]['title'][:33]
            print(f"{i:<6} {title:<35} {count:<15}")
    
    print("="*60)

def overdue_books_report():
    print("\n--- Overdue Books Report ---")
    
    borrowed_books = get_borrowed_books()
    students = get_students()
    books = get_books()
    today = datetime.now()
    
    print("\n" + "="*70)
    print(f"{'Student Name':<25} {'Book Title':<30} {'Days Overdue':<15}")
    print("-"*70)
    
    overdue_found = False
    for record in borrowed_books.values():
        if not record['returned']:
            due_date = datetime.strptime(record['due_date'], "%Y-%m-%d")
            if today > due_date:
                overdue_found = True
                student_name = students[record['student_id']]['name'][:23]
                book_title = books[record['book_id']]['title'][:28]
                days_overdue = (today - due_date).days
                print(f"{student_name:<25} {book_title:<30} {days_overdue:<15}")
    
    if not overdue_found:
        print("No overdue books!")
    
    print("="*70)

def books_per_school():
    print("\n--- Books Per School Report ---")
    
    books = get_books()
    borrowed_books = get_borrowed_books()
    
    total_books = len(books)
    total_copies = sum(book['quantity'] for book in books.values())
    currently_borrowed = sum(1 for r in borrowed_books.values() if not r['returned'])
    
    print("\n" + "="*40)
    print(f"Total Unique Books: {total_books}")
    print(f"Total Book Copies: {total_copies}")
    print(f"Currently Borrowed: {currently_borrowed}")
    print(f"Available: {total_copies - currently_borrowed}")
    print("="*40)

def student_borrow_history():
    print("\n--- Student Borrow History ---")
    
    student_id = input("Enter Student ID: ")
    
    students = get_students()
    books = get_books()
    borrowed_books = get_borrowed_books()
    
    if student_id not in students:
        print("✗ Student not found!")
        return
    
    student = students[student_id]
    print(f"\n{'='*60}")
    print(f"Borrow History for: {student['name']}")
    print(f"Student ID: {student_id}")
    print(f"{'='*60}")
    
    history_found = False
    for borrow_id, record in borrowed_books.items():
        if record['student_id'] == student_id:
            history_found = True
            book_title = books[record['book_id']]['title']
            status = "✓ Returned" if record['returned'] else "Borrowed"
            
            print(f"\nBook: {book_title}")
            print(f"Borrow Date: {record['borrow_date']}")
            print(f"Due Date: {record['due_date']}")
            print(f"Status: {status}")
            
            if record['returned']:
                print(f"Return Date: {record.get('return_date', 'N/A')}")
            elif record.get('overdue'):
                print("⚠ OVERDUE")
            
            print("-"*60)
    
    if not history_found:
        print("\nNo borrow history found for this student.")
    
    print("="*60)

def reporting_menu():
    while True:
        print("\n" + "="*50)
        print("=== Reporting ===")
        print("="*50)
        print("1. Most Borrowed Books")
        print("2. Overdue Books Report")
        print("3. Books per School")
        print("4. Student Borrow History")
        print("5. Back to Main Menu")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            most_borrowed_books()
        elif choice == '2':
            overdue_books_report()
        elif choice == '3':
            books_per_school()
        elif choice == '4':
            student_borrow_history()
        elif choice == '5':
            break
        else:
            print("Invalid choice!")