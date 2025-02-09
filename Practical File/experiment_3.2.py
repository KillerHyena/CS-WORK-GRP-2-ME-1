#Use dictionaries to store and retrieve student grades
def add_student(student_grades):
    name = input("Enter student name: ")
    grade = float(input(f"Enter grade for {name}: "))
    student_grades[name] = grade
    print(f"{name} added successfully!\n")
def display_students(student_grades):
    if not student_grades:
        print("No student records found.\n")
        return
    print("\nStudent Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")
    print()
def search_student(student_grades):
    search_name = input("\nEnter student name to retrieve grade: ")
    if search_name in student_grades:
        print(f"{search_name}'s Grade: {student_grades[search_name]}\n")
    else:
        print(f"Student {search_name} not found.\n")
def main():
    student_grades = {}   
    while True:
        print("Menu:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search for a Student")
        print("4. Exit")
        choice = input("Enter your choice: ")      
        if choice == '1':
            add_student(student_grades)
        elif choice == '2':
            display_students(student_grades)
        elif choice == '3':
            search_student(student_grades)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()