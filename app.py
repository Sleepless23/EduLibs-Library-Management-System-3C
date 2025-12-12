from auth import user_login
from menu import main_menu, user_menu

def main():
    print("\n" + "="*50)
    print("  EDULIBS LIBRARY MANAGEMENT SYSTEM - 3C")
    print("="*50)
    
    while True:
        result = user_login()
        if result:
            role, user_id = result
            
            if role == 'admin':
                main_menu(role, user_id)
            else: 
                user_menu(user_id)
            
            continue_choice = input("\nReturn to login? (yes/no): ")
            if continue_choice.lower() != 'yes':
                print("\n" + "="*50)
                print("Thank you for using EduLibs!")
                print("System ended.")
                print("="*50)
                break

if __name__ == "__main__":
    main()