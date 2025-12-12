import json
import os

BOOKS_FILE = 'data/books.json'
STUDENTS_FILE = 'data/students.json'
BORROWED_FILE = 'data/borrowed_books.json'

def ensure_data_directory():
    if not os.path.exists('data'):
        os.makedirs('data')

def load_data(file_path):
    ensure_data_directory()

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("{}")
        return {}

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, ValueError):
        return {}

def save_data(filename, data):
    ensure_data_directory()
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_books():
    return load_data(BOOKS_FILE)

def save_books(books):
    save_data(BOOKS_FILE, books)

def get_students():
    return load_data(STUDENTS_FILE)

def save_students(students):
    save_data(STUDENTS_FILE, students)

def get_borrowed_books():
    return load_data(BORROWED_FILE)

def save_borrowed_books(borrowed):
    save_data(BORROWED_FILE, borrowed)