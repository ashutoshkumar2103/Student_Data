# Initialize empty dictionary to store student names and grades
student_list = {}

# Functionality to add, update, and print student grades using while loop
while True:
    print("\nMenu:")
    print("1. Add New Student")
    print("2. Update Student Grade")
    print("3. Print All Students")
    print("4. Exit")

    # Get user choice
    choice = input("Enter your choice (1-4): ")

# Process the user's choice
# Add new student
    if choice == '1':
        name = input("Enter student name: ")
        if name in student_list:
            print("Student already exists.")
        else:
            grade = input("Enter grade: ")
            student_list[name] = grade
            print(f"Added {name} with grade {grade}.")

# Update existing student's grade
    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_list:
            grade = input("Enter new grade: ")
            student_list[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print("Student not found.")

# Print all students and their grades
    elif choice == '3':
        if student_list:
            print("\nStudent Grades:")
            for name, grade in student_list.items():
                print(f"{name}: {grade}")
        else:
            print("No student records found.")

# Exit the 
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break

# if the choice is invalid, this shall print an error message
    else:
        print("Invalid choice. Please select between 1 to 4.")




# End of the program