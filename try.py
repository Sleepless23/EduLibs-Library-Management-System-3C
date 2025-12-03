def login():
    print("=== LOGIN ===")
    username = input("Enter username: ")
    role = input("Enter role (librarian/admin): ")
    return role

def add_new_book():
    print("Add New Book")


def edit_book_info():
    print("Edit Book Info")

def delete_book():
    print("Delete Book")

def book_management():
    while True:
        print("\n--- BOOK MANAGEMENT ---")
        print("[1] Add New Book")
        print("[2] Edit Book Info")
        print("[3] Delete Book")
        print("[0] Back")
        choice = input("Select: ")

        if choice == "1":
            add_new_book()
        elif choice == "2":
            edit_book_info()
        elif choice == "3":
            delete_book()
        elif choice == "0":
            break

def register_student():
    print("Register Student")

def edit_student_details():
    print("Edit Student Details")

def student_management():
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("[1] Register Student")
        print("[2] Edit Student Details")
        print("[0] Back")
        choice = input("Select: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            edit_student_details()
        elif choice == "0":
            break

def borrow_book():
    print("Borrow Book")

def check_availability():
    print("Checking availability")

def return_book():
    print("Returning book")

def check_overdue():
    print("Checking overdue")

def borrow_return():
    while True:
        print("\n--- BORROW / RETURN ---")
        print("[1] Borrow Book")
        print("[2] Check Availability")
        print("[3] Return Book")
        print("[4] Check Overdue")
        print("[0] Back")
        choice = input("Select: ")

        if choice == "1":
            borrow_book()
        elif choice == "2":
            check_availability()
        elif choice == "3":
            return_book()
        elif choice == "4":
            check_overdue()
        elif choice == "0":
            break


def report_most_borrowed():
    print("Report: Most Borrowed Books")

def report_overdue_books():
    print("Report: Overdue Books")

def report_books_per_school():
    print("Report: Books Per School")

def report_student_history():
    print("Report: Student Borrow History")

def reporting():
    while True:
        print("\n--- REPORTING ---")
        print("[1] Most Borrowed Books")
        print("[2] Overdue Books Report")
        print("[3] Books Per School")
        print("[4] Student Borrow History")
        print("[0] Back")
        choice = input("Select: ")

        if choice == "1":
            report_most_borrowed()
        elif choice == "2":
            report_overdue_books()
        elif choice == "3":
            report_books_per_school()
        elif choice == "4":
            report_student_history()
        elif choice == "0":
            break


def main_menu(role):
    while True:
        print("\n========= MAIN MENU =========")
        print("[1] Book Management")
        print("[2] Student Management")
        print("[3] Borrow / Return")
        print("[4] Reporting")
        print("[5] Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            book_management()
        elif choice == "2":
            student_management()
        elif choice == "3":
            borrow_return()
        elif choice == "4":
            reporting()
        elif choice == "5":
            print("Logging out...")
            break



def start():
    role = login()
    main_menu(role)
    print("End.")

start()