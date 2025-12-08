from data_manager import get_students, save_students


ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def register_user():
    print("\n=== User Registration ===")
    students = get_students()
    
    student_id = input("Create your Student ID: ")
    
    if student_id in students:
        print("✗ Student ID already exists! Please try logging in.")
        return None
    
  
    name = input("Enter your Full Name: ")
    class_name = input("Enter your Class: ")
    school = input("Enter your School: ")
    contact = input("Enter your Contact Number: ")
    password = input("Create a Password: ")
    
 
    students[student_id] = {
        'name': name,
        'class': class_name,
        'school': school,
        'contact': contact,
        'password': password,
        'books_borrowed': []
    }
    
    save_students(students)
    print("\n✓ Registration successful!")
    print(f"Your Student ID is: {student_id}")
    return student_id

def user_login_process():
    print("\n=== User Login ===")
    students = get_students()
    
    student_id = input("Enter Student ID: ")
    password = input("Enter Password: ")
    
    if student_id not in students:
        print("✗ Student ID not found!")
        return None
    
    if students[student_id]['password'] != password:
        print("✗ Incorrect password!")
        return None
    
    print(f"✓ Welcome back, {students[student_id]['name']}!")
    return ('user', student_id)

def admin_login_process():
    print("\n=== Admin Login ===")
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")
    
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("✓ Admin login successful!")
        return ('admin', None)
    else:
        print("✗ Invalid admin credentials!")
        return None

def user_login():
    while True:
        print("\n" + "="*50)
        print("=== EduLibs Authentication ===")
        print("="*50)
        print("1. User Login")
        print("2. User Registration")
        print("3. Admin Login")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ")
        
        if choice == '1':
            result = user_login_process()
            if result:
                return result
        elif choice == '2':
            student_id = register_user()
            if student_id:
                return ('user', student_id)
        elif choice == '3':
            result = admin_login_process()
            if result:
                return result
        elif choice == '4':
            print("\nGoodbye!")
            exit()
        else:
            print("✗ Invalid choice!")
