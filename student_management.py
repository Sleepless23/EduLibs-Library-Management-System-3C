from data_manager import get_students, save_students

def view_all_students():
    print("\n--- All Registered Students ---")
    students = get_students()
    
    if not students:
        print("No students registered yet!")
        return
    
    print("\n" + "="*80)
    print(f"{'ID':<15} {'Name':<25} {'Class':<15} {'School':<25}")
    print("-"*80)
    
    for student_id, info in students.items():
        print(f"{student_id:<15} {info['name']:<25} {info.get('class', 'N/A'):<15} {info.get('school', 'N/A'):<25}")
    
    print("="*80)

def register_student():
    print("\n--- Register Student (Admin) ---")
    students = get_students()
    
    student_id = input("Enter Student ID: ")
    
    if student_id in students:
        print("Student ID already exists!")
        return
    
    name = input("Enter Student Name: ")
    class_name = input("Enter Class: ")
    school = input("Enter School: ")
    contact = input("Enter Contact: ")
    password = input("Set Password for Student: ")
    
    students[student_id] = {
        'name': name,
        'class': class_name,
        'school': school,
        'contact': contact,
        'password': password,
        'books_borrowed': []
    }
    
    save_students(students)
    print("✓ Student registered successfully!")

def edit_student_details():
    print("\n--- Edit Student Details ---")
    students = get_students()
    
    student_id = input("Enter Student ID: ")
    
    if student_id not in students:
        print("Student not found!")
        return
    
    student = students[student_id]
    print(f"\nCurrent info:")
    print(f"Name: {student['name']}")
    print(f"Class: {student.get('class', 'N/A')}")
    print(f"School: {student.get('school', 'N/A')}")
    print(f"Contact: {student.get('contact', 'N/A')}")
    print("\nLeave blank to keep current value")
    
    name = input("Enter new Name: ")
    class_name = input("Enter new Class: ")
    school = input("Enter new School: ")
    contact = input("Enter new Contact: ")
    
    if name:
        students[student_id]['name'] = name
    if class_name:
        students[student_id]['class'] = class_name
    if school:
        students[student_id]['school'] = school
    if contact:
        students[student_id]['contact'] = contact
    
    save_students(students)
    print("✓ Student info updated!")

def student_management_menu():
    while True:
        print("\n" + "="*50)
        print("=== Student Management ===")
        print("="*50)
        print("1. View All Students")
        print("2. Register Student")
        print("3. Edit Student Details")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter choice: ")
        
        if choice == '1':
            view_all_students()
        elif choice == '2':
            register_student()
        elif choice == '3':
            edit_student_details()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")