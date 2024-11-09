import mysql.connector
from prettytable import PrettyTable

# Function to connect to the database
def connect_to_database():
    try:
        return mysql.connector.connect(host="localhost", user="root", password="rahul2401", database="student_management")
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Function to display student details
def student_details():
    while True:
        print("\nStudent Details Menu")
        print("1. Display All Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Back to Main Menu")
        print("7. Exit")

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            display_all_students()
        elif choice == 2:
            add_student()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            search_student()
        elif choice == 6:
            break  # Back to main menu
        elif choice == 7:
            exit_program()
        else:
            print("Invalid choice")

# Function to display all students
def display_all_students():
    try:
        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()

            # Create a pretty table object
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Address", "Performance", "Attendance", "Department ID"]

            # Add rows to the pretty table
            for student in students:
                table.add_row(student)

            # Print the pretty table
            print(table)
    except Exception as e:
        print(f"Error displaying students: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to add a new student
def add_student():
    try:
        name = input("Enter student name: ")
        address = input("Enter student address: ")
        performance = input("Enter student performance: ")
        attendance = input("Enter student attendance: ")
        department_id = int(input("Enter department ID: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("INSERT INTO students (name, address, performance, attendance, department_id) VALUES (%s, %s, %s, %s, %s)", 
                           (name, address, performance, attendance, department_id))
            mycon.commit()
            print("Student added successfully!")
    except Exception as e:
        print(f"Error adding student: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to update a student record
def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
        name = input("Enter new student name: ")
        address = input("Enter new student address: ")
        performance = input("Enter new student performance: ")
        attendance = input("Enter new student attendance: ")
        department_id = int(input("Enter new department ID: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("UPDATE students SET name = %s, address = %s, performance = %s, attendance = %s, department_id = %s WHERE id = %s",
                           (name, address, performance, attendance, department_id, student_id))
            mycon.commit()
            print("Student updated successfully!")
    except Exception as e:
        print(f"Error updating student: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to delete a student record
def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()

            # Delete related grades first
            cursor.execute("DELETE FROM grades WHERE student_id = %s", (student_id,))
            mycon.commit()

            # Then delete the student record
            cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            mycon.commit()

            print("Student deleted successfully!")
    except Exception as e:
        print(f"Error deleting student: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()


# Function to search for a student
def search_student():
    try:
        name = input("Enter student name to search: ")

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("SELECT * FROM students WHERE name LIKE %s", ('%' + name + '%',))
            students = cursor.fetchall()

            if students:
                # Create a pretty table object for displaying the student details
                table = PrettyTable()
                table.field_names = ["ID", "Name", "Address", "Performance", "Attendance", "Department ID"]
                for student in students:
                    table.add_row(student)

                # Print the pretty table
                print(table)
            else:
                print("No student found with the provided name.")
    except Exception as e:
        print(f"Error searching for student: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to display department details
def department_details():
    while True:
        print("\nDepartment Details Menu")
        print("1. Show Departments")
        print("2. Add Department")
        print("3. Delete Department")
        print("4. Back to Main Menu")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_departments()
        elif choice == 2:
            add_department()
        elif choice == 3:
            delete_department()
        elif choice == 4:
            break  # Back to main menu
        elif choice == 5:
            exit_program()
        else:
            print("Invalid choice")

# Function to display all departments
def show_departments():
    try:
        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("SELECT * FROM departments")
            departments = cursor.fetchall()

            # Create a pretty table object
            table = PrettyTable()
            table.field_names = ["ID", "Name"]

            # Add rows to the pretty table
            for department in departments:
                table.add_row(department)

            # Print the pretty table
            print(table)
    except Exception as e:
        print(f"Error displaying departments: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to add a new department
def add_department():
    try:
        name = input("Enter department name: ")

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("INSERT INTO departments (name) VALUES (%s)", (name,))
            mycon.commit()
            print("Department added successfully!")
    except Exception as e:
        print(f"Error adding department: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to delete a department
def delete_department():
    try:
        department_id = int(input("Enter department ID to delete: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("DELETE FROM departments WHERE id = %s", (department_id,))
            mycon.commit()
            print("Department deleted successfully!")
    except Exception as e:
        print(f"Error deleting department: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to display course details
def course_details():
    while True:
        print("\nCourse Details Menu")
        print("1. Show All Courses")
        print("2. Add Course")
        print("3. Delete Course")
        print("4. Back to Main Menu")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_all_courses()
        elif choice == 2:
            add_course()
        elif choice == 3:
            delete_course()
        elif choice == 4:
            break  # Back to main menu
        elif choice == 5:
            exit_program()
        else:
            print("Invalid choice")

# Function to display all courses
def show_all_courses():
    try:
        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("SELECT * FROM courses")  # Retrieve all columns
            courses = cursor.fetchall()

            # Create a pretty table object
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Department ID"]

            # Add rows to the pretty table
            for course in courses:
                table.add_row(course)

            # Print the pretty table
            print(table)
    except Exception as e:
        print(f"Error displaying courses: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()


# Function to add a new course
def add_course():
    try:
        course_name = input("Enter course name: ")
        department_id = int(input("Enter department ID: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("INSERT INTO courses (course_name, department_id) VALUES (%s, %s)", (course_name, department_id))
            mycon.commit()
            print("Course added successfully!")
    except Exception as e:
        print(f"Error adding course: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()


# Function to delete a course
def delete_course():
    try:
        course_id = int(input("Enter course ID to delete: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))
            mycon.commit()
            print("Course deleted successfully!")
    except Exception as e:
        print(f"Error deleting course: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

from prettytable import PrettyTable

# Function to display grade details
def grade_details():
    while True:
        print("\nGrade Details Menu")
        print("1. Show Grades of a Student")
        print("2. Add Grade")
        print("3. Delete Grade")
        print("4. View Most Grades")
        print("5. View Least Grades")
        print("6. Back to Main Menu")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_student_grades()
        elif choice == 2:
            add_grade()
        elif choice == 3:
            delete_grade()
        elif choice == 4:
            view_most_grades()
        elif choice == 5:
            view_least_grades()
        elif choice == 6:
            break  # Back to main menu
        elif choice == 7:
            exit_program()
        else:
            print("Invalid choice")

# Function to add a new grade
def add_grade():
    try:
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        grade = input("Enter grade: ")

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)",
                           (student_id, course_id, grade))
            mycon.commit()
            print("Grade added successfully!")
    except Exception as e:
        print(f"Error adding grade: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to delete a grade
def delete_grade():
    try:
        grade_id = int(input("Enter grade ID to delete: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("DELETE FROM grades WHERE id = %s", (grade_id,))
            mycon.commit()
            print("Grade deleted successfully!")
    except Exception as e:
        print(f"Error deleting grade: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to show grades of a particular student
def show_student_grades():
    try:
        student_id = int(input("Enter student ID to show grades: "))

        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("SELECT student_id, course_id, grade FROM grades WHERE student_id = %s", (student_id,))
            grades = cursor.fetchall()

            # Create a pretty table object
            table = PrettyTable()
            table.field_names = ["Student ID", "Course ID", "Grade"]

            # Add rows to the pretty table
            for grade in grades:
                table.add_row(grade)

            # Print the pretty table
            print(table)
    except Exception as e:
        print(f"Error displaying student grades: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()


# Function to view the most frequent grade
def view_most_grades():
    try:
        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("SELECT grade, COUNT(*) AS frequency FROM grades GROUP BY grade ORDER BY frequency DESC LIMIT 1")
            most_grade = cursor.fetchone()

            if most_grade:
                print("Most frequent grade:", most_grade[0])
                print("Frequency:", most_grade[1])
            else:
                print("No grades found.")
    except Exception as e:
        print(f"Error viewing most frequent grade: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()

# Function to view the least frequent grade
def view_least_grades():
    try:
        mycon = connect_to_database()
        if mycon:
            cursor = mycon.cursor()
            cursor.execute("SELECT grade, COUNT(*) AS frequency FROM grades GROUP BY grade ORDER BY frequency ASC LIMIT 1")
            least_grade = cursor.fetchone()

            if least_grade:
                print("Least frequent grade:", least_grade[0])
                print("Frequency:", least_grade[1])
            else:
                print("No grades found.")
    except Exception as e:
        print(f"Error viewing least frequent grade: {e}")
    finally:
        if mycon and mycon.is_connected():
            cursor.close()
            mycon.close()


# Function to exit the program
def exit_program():
    print("Exiting the program.")
    exit()


# Main function
def main():
    while True:
        print("Welcome to the Student Management System!")
        print("This system allows you to manage student records, courses, grades, and departments.")
        print("You can perform various operations such as adding, updating, deleting, and searching for student records, as well as managing courses and grades.")
        print("Additionally, you can view statistics such as the average grade and the least frequent grades.")
        print("Use the menu options to navigate through the system.")
        print("Menu Options:")
        print("1. Student Details")
        print("2. Department Details")
        print("3. Course Details")
        print("4. Grade Details")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_details()
        elif choice == 2:
            department_details()
        elif choice == 3:
            course_details()
        elif choice == 4:
            grade_details()
        elif choice == 5:
            exit_program()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
