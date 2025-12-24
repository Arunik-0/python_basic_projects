students = []

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully.")

def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    for s in students:
        print("ID:", s["id"], "| Name:", s["name"],
              "| Age:", s["age"], "| Branch:", s["branch"])

def search_student():
    search_id = input("Enter student ID to search: ")

    for s in students:
        if s["id"] == search_id:
            print("Student found:")
            print(s)
            return

    print("Student not found.")

def delete_student():
    delete_id = input("Enter student ID to delete: ")

    for s in students:
        if s["id"] == delete_id:
            students.remove(s)
            print("Student deleted.")
            return

    print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")