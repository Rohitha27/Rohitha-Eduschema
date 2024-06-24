from database import Database
from models import Course, Instructor, Student, Assessment, Enrollment

def main_menu():
    print("\n===== Main Menu =====")
    print("1. Course Management")
    print("2. Instructor Management")
    print("3. Student Management")
    print("4. Assessment Management")
    print("5. Enrollment Management")
    print("6. View Deleted Entries")
    print("7. Exit")

def course_management_menu(db):
    while True:
        print("\n===== Course Management Menu =====")
        print("1. Create Course")
        print("2. Update Course")
        print("3. Delete Course")
        print("4. List Courses")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            course_name = input("Enter course name: ")
            course_description = input("Enter course description: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            Course.create_course(db, course_name, course_description, start_date, end_date)
            print("Course created successfully!")
        elif choice == '2':
            course_id = int(input("Enter course ID to update: "))
            course_name = input("Enter updated course name: ")
            course_description = input("Enter updated course description: ")
            start_date = input("Enter updated start date (YYYY-MM-DD): ")
            end_date = input("Enter updated end date (YYYY-MM-DD): ")
            Course.update_course(db, course_id, course_name, course_description, start_date, end_date)
            print("Course updated successfully!")
        elif choice == '3':
            course_id = int(input("Enter course ID to delete: "))
            Course.delete_course(db, course_id)
            print("Course deleted successfully!")
        elif choice == '4':
            courses = Course.get_courses(db)
            if courses:
                print("\n===== List of Courses =====")
                for course in courses:
                    print(f"Course ID: {course[0]}, Name: {course[1]}, Description: {course[2]}, Start Date: {course[3]}, End Date: {course[4]}")
            else:
                print("No courses found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def instructor_management_menu(db):
    while True:
        print("\n===== Instructor Management Menu =====")
        print("1. Create Instructor")
        print("2. Update Instructor")
        print("3. Delete Instructor")
        print("4. List Instructors")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            instructor_name = input("Enter instructor name: ")
            instructor_email = input("Enter instructor email: ")
            Instructor.create_instructor(db, instructor_name, instructor_email)
            print("Instructor created successfully!")
        elif choice == '2':
            instructor_id = int(input("Enter instructor ID to update: "))
            instructor_name = input("Enter updated instructor name: ")
            instructor_email = input("Enter updated instructor email: ")
            Instructor.update_instructor(db, instructor_id, instructor_name, instructor_email)
            print("Instructor updated successfully!")
        elif choice == '3':
            instructor_id = int(input("Enter instructor ID to delete: "))
            Instructor.delete_instructor(db, instructor_id)
            print("Instructor deleted successfully!")
        elif choice == '4':
            instructors = Instructor.get_instructors(db)
            if instructors:
                print("\n===== List of Instructors =====")
                for instructor in instructors:
                    print(f"Instructor ID: {instructor[0]}, Name: {instructor[1]}, Email: {instructor[2]}")
            else:
                print("No instructors found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def student_management_menu(db):
    while True:
        print("\n===== Student Management Menu =====")
        print("1. Create Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter student name: ")
            student_email = input("Enter student email: ")
            Student.create_student(db, student_name, student_email)
            print("Student created successfully!")
        elif choice == '2':
            student_id = int(input("Enter student ID to update: "))
            student_name = input("Enter updated student name: ")
            student_email = input("Enter updated student email: ")
            Student.update_student(db, student_id, student_name, student_email)
            print("Student updated successfully!")
        elif choice == '3':
            student_id = int(input("Enter student ID to delete: "))
            Student.delete_student(db, student_id)
            print("Student deleted successfully!")
        elif choice == '4':
            students = Student.get_students(db)
            if students:
                print("\n===== List of Students =====")
                for student in students:
                    print(f"Student ID: {student[0]}, Name: {student[1]}, Email: {student[2]}")
            else:
                print("No students found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def assessment_management_menu(db):
    while True:
        print("\n===== Assessment Management Menu =====")
        print("1. Create Assessment")
        print("2. Update Assessment")
        print("3. Delete Assessment")
        print("4. List Assessments")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            course_id = int(input("Enter course ID for the assessment: "))
            assessment_name = input("Enter assessment name: ")
            assessment_date = input("Enter assessment date (YYYY-MM-DD): ")
            Assessment.create_assessment(db, course_id, assessment_name, assessment_date)
            print("Assessment created successfully!")
        elif choice == '2':
            assessment_id = int(input("Enter assessment ID to update: "))
            course_id = int(input("Enter updated course ID for the assessment: "))
            assessment_name = input("Enter updated assessment name: ")
            assessment_date = input("Enter updated assessment date (YYYY-MM-DD): ")
            Assessment.update_assessment(db, assessment_id, course_id, assessment_name, assessment_date)
            print("Assessment updated successfully!")
        elif choice == '3':
            assessment_id = int(input("Enter assessment ID to delete: "))
            Assessment.delete_assessment(db, assessment_id)
            print("Assessment deleted successfully!")
        elif choice == '4':
            assessments = Assessment.get_assessments_by_course(db)
            if assessments:
                print("\n===== List of Assessments =====")
                for assessment in assessments:
                    print(f"Assessment ID: {assessment[0]}, Course ID: {assessment[1]}, Name: {assessment[2]}, Date: {assessment[3]}")
            else:
                print("No assessments found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def enrollment_management_menu(db):
    while True:
        print("\n===== Enrollment Management Menu =====")
        print("1. Enroll Student")
        print("2. Update Enrollment")
        print("3. Withdraw Student")
        print("4. List Enrollments")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = int(input("Enter student ID to enroll: "))
            course_id = int(input("Enter course ID to enroll in: "))
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            Enrollment.enroll_student(db, student_id, course_id, enrollment_date)
            print("Student enrolled successfully!")
        elif choice == '2':
            enrollment_id = int(input("Enter enrollment ID to update: "))
            student_id = int(input("Enter updated student ID: "))
            course_id = int(input("Enter updated course ID: "))
            enrollment_date = input("Enter updated enrollment date (YYYY-MM-DD): ")
            completion_status = input("Enter updated completion status (e.g., 'In Progress', 'Completed'): ")
            Enrollment.update_enrollment(db, enrollment_id, student_id, course_id, enrollment_date, completion_status)
            print("Enrollment updated successfully!")
        elif choice == '3':
            enrollment_id = int(input("Enter enrollment ID to withdraw: "))
            Enrollment.delete_enrollment(db, enrollment_id)
            print("Student withdrawn from course successfully!")
        elif choice == '4':
            enrollments = Enrollment.get_enrollments_by_course(db)
            if enrollments:
                print("\n===== List of Enrollments =====")
                for enrollment in enrollments:
                    print(f"Enrollment ID: {enrollment[0]}, Student ID: {enrollment[1]}, Course ID: {enrollment[2]}, Enrollment Date: {enrollment[3]}, Completion Status: {enrollment[4]}")
            else:
                print("No enrollments found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def view_deleted_entries(db):
    while True:
        print("\n===== View Deleted Entries =====")
        print("1. Deleted Courses")
        print("2. Deleted Instructors")
        print("3. Deleted Students")
        print("4. Deleted Assessments")
        print("5. Deleted Enrollments")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            deleted_courses = Course.get_deleted_courses(db)
            if deleted_courses:
                print("\n===== Deleted Courses =====")
                for course in deleted_courses:
                    print(f"Course ID: {course[0]}, Name: {course[1]}, Description: {course[2]}, Start Date: {course[3]}, End Date: {course[4]}")
            else:
                print("No deleted courses found.")
        elif choice == '2':
            deleted_instructors = Instructor.get_deleted_instructors(db)
            if deleted_instructors:
                print("\n===== Deleted Instructors =====")
                for instructor in deleted_instructors:
                    print(f"Instructor ID: {instructor[0]}, Name: {instructor[1]}, Email: {instructor[2]}")
            else:
                print("No deleted instructors found.")
        elif choice == '3':
            deleted_students = Student.get_deleted_students(db)
            if deleted_students:
                print("\n===== Deleted Students =====")
                for student in deleted_students:
                    print(f"Student ID: {student[0]}, Name: {student[1]}, Email: {student[2]}")
            else:
                print("No deleted students found.")
        elif choice == '4':
            deleted_assessments = Assessment.get_deleted_assessments(db)
            if deleted_assessments:
                print("\n===== Deleted Assessments =====")
                for assessment in deleted_assessments:
                    print(f"Assessment ID: {assessment[0]}, Course ID: {assessment[1]}, Name: {assessment[2]}, Date: {assessment[3]}")
            else:
                print("No deleted assessments found.")
        elif choice == '5':
            deleted_enrollments = Enrollment.get_deleted_enrollments(db)
            if deleted_enrollments:
                print("\n===== Deleted Enrollments =====")
                for enrollment in deleted_enrollments:
                    print(f"Enrollment ID: {enrollment[0]}, Student ID: {enrollment[1]}, Course ID: {enrollment[2]}, Enrollment Date: {enrollment[3]}, Completion Status: {enrollment[4]}")
            else:
                print("No deleted enrollments found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    db = Database(host='localhost', user='your_username', password='your_password', database='your_database')

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            course_management_menu(db)
        elif choice == '2':
            instructor_management_menu(db)
        elif choice == '3':
            student_management_menu(db)
        elif choice == '4':
            assessment_management_menu(db)
        elif choice == '5':
            enrollment_management_menu(db)
        elif choice == '6':
            view_deleted_entries(db)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            db.close_connection()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
