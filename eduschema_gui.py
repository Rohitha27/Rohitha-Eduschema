import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import Database
from models import Course, Instructor, Student, Assessment, Enrollment
import datetime

class EduSchemaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EduSchema - Online Learning Platform")
        self.db = Database(host="localhost", user="your_username", password="your_password", database="edu_schema")

        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()

        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(pady=10)

        # Initialize dictionaries to store currently displayed data
        self.courses_displayed = []
        self.instructors_displayed = []
        self.students_displayed = []
        self.assessments_displayed = []
        self.enrollments_displayed = []

        # Create tabs
        self.create_course_tab()
        self.create_instructor_tab()
        self.create_student_tab()
        self.create_assessment_tab()
        self.create_enrollment_tab()

    def clear_displayed_data(self):
        # Clear currently displayed data in all tabs
        self.courses_displayed.clear()
        self.instructors_displayed.clear()
        self.students_displayed.clear()
        self.assessments_displayed.clear()
        self.enrollments_displayed.clear()

    def refresh_display(self):
        # Refresh currently displayed data in all tabs
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab == 0:
            self.list_courses()
        elif current_tab == 1:
            self.list_instructors()
        elif current_tab == 2:
            self.list_students()
        elif current_tab == 3:
            self.list_assessments()
        elif current_tab == 4:
            self.list_enrollments()

    def create_course_tab(self):
        course_tab = ttk.Frame(self.notebook)
        self.notebook.add(course_tab, text="Courses")

        # Course Management UI elements
        tk.Label(course_tab, text="Course Management", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        tk.Label(course_tab, text="Course Name:").grid(row=1, column=0, padx=10, pady=5)
        self.course_name_entry = tk.Entry(course_tab)
        self.course_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(course_tab, text="Course Description:").grid(row=2, column=0, padx=10, pady=5)
        self.course_description_entry = tk.Text(course_tab, height=5, width=30)
        self.course_description_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(course_tab, text="Start Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.start_date_entry = tk.Entry(course_tab)
        self.start_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(course_tab, text="End Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
        self.end_date_entry = tk.Entry(course_tab)
        self.end_date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Buttons
        add_button = tk.Button(course_tab, text="Add Course", command=self.add_course)
        add_button.grid(row=5, column=0, padx=10, pady=10)

        update_button = tk.Button(course_tab, text="Update Course", command=self.update_course)
        update_button.grid(row=5, column=1, padx=10, pady=10)

        delete_button = tk.Button(course_tab, text="Delete Course", command=self.delete_course)
        delete_button.grid(row=5, column=2, padx=10, pady=10)

        list_button = tk.Button(course_tab, text="Refresh List", command=self.list_courses)
        list_button.grid(row=5, column=3, padx=10, pady=10)

        # Listbox for displaying courses
        self.course_listbox = tk.Listbox(course_tab, height=10, width=100)
        self.course_listbox.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(course_tab, orient="vertical")
        scrollbar.config(command=self.course_listbox.yview)
        scrollbar.grid(row=6, column=4, sticky="ns")

        self.course_listbox.config(yscrollcommand=scrollbar.set)

    def add_course(self):
        course_name = self.course_name_entry.get()
        course_description = self.course_description_entry.get("1.0", tk.END)
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        try:
            Course.create_course(self.db, course_name, course_description, start_date, end_date)
            messagebox.showinfo("Success", "Course added successfully!")
            self.refresh_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_course(self):
        selected_course = self.course_listbox.curselection()
        if selected_course:
            course_id = self.courses_displayed[selected_course[0]][0]
            course_name = self.course_name_entry.get()
            course_description = self.course_description_entry.get("1.0", tk.END)
            start_date = self.start_date_entry.get()
            end_date = self.end_date_entry.get()
            try:
                Course.update_course(self.db, course_id, course_name, course_description, start_date, end_date)
                messagebox.showinfo("Success", "Course updated successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a course to update.")

    def delete_course(self):
        selected_course = self.course_listbox.curselection()
        if selected_course:
            course_id = self.courses_displayed[selected_course[0]][0]
            try:
                Course.delete_course(self.db, course_id)
                messagebox.showinfo("Success", "Course deleted successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a course to delete.")

    def list_courses(self):
        self.clear_displayed_data()
        self.course_listbox.delete(0, tk.END)
        courses = Course.get_courses(self.db)
        if courses:
            for course in courses:
                self.courses_displayed.append(course)
                course_info = f"ID: {course[0]}, Name: {course[1]}, Start Date: {course[3]}, End Date: {course[4]}"
                self.course_listbox.insert(tk.END, course_info)
        else:
            self.course_listbox.insert(tk.END, "No courses found.")

    def create_instructor_tab(self):
        instructor_tab = ttk.Frame(self.notebook)
        self.notebook.add(instructor_tab, text="Instructors")

        # Instructor Management UI elements
        tk.Label(instructor_tab, text="Instructor Management", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        tk.Label(instructor_tab, text="Instructor Name:").grid(row=1, column=0, padx=10, pady=5)
        self.instructor_name_entry = tk.Entry(instructor_tab)
        self.instructor_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(instructor_tab, text="Instructor Email:").grid(row=2, column=0, padx=10, pady=5)
        self.instructor_email_entry = tk.Entry(instructor_tab)
        self.instructor_email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        add_button = tk.Button(instructor_tab, text="Add Instructor", command=self.add_instructor)
        add_button.grid(row=3, column=0, padx=10, pady=10)

        update_button = tk.Button(instructor_tab, text="Update Instructor", command=self.update_instructor)
        update_button.grid(row=3, column=1, padx=10, pady=10)

        delete_button = tk.Button(instructor_tab, text="Delete Instructor", command=self.delete_instructor)
        delete_button.grid(row=3, column=2, padx=10, pady=10)

        list_button = tk.Button(instructor_tab, text="Refresh List", command=self.list_instructors)
        list_button.grid(row=3, column=3, padx=10, pady=10)

        # Listbox for displaying instructors
        self.instructor_listbox = tk.Listbox(instructor_tab, height=10, width=100)
        self.instructor_listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(instructor_tab, orient="vertical")
        scrollbar.config(command=self.instructor_listbox.yview)
        scrollbar.grid(row=4, column=4, sticky="ns")

        self.instructor_listbox.config(yscrollcommand=scrollbar.set)

    def add_instructor(self):
        instructor_name = self.instructor_name_entry.get()
        instructor_email = self.instructor_email_entry.get()
        try:
            Instructor.create_instructor(self.db, instructor_name, instructor_email)
            messagebox.showinfo("Success", "Instructor added successfully!")
            self.refresh_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_instructor(self):
        selected_instructor = self.instructor_listbox.curselection()
        if selected_instructor:
            instructor_id = self.instructors_displayed[selected_instructor[0]][0]
            instructor_name = self.instructor_name_entry.get()
            instructor_email = self.instructor_email_entry.get()
            try:
                Instructor.update_instructor(self.db, instructor_id, instructor_name, instructor_email)
                messagebox.showinfo("Success", "Instructor updated successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select an instructor to update.")

    def delete_instructor(self):
        selected_instructor = self.instructor_listbox.curselection()
        if selected_instructor:
            instructor_id = self.instructors_displayed[selected_instructor[0]][0]
            try:
                Instructor.delete_instructor(self.db, instructor_id)
                messagebox.showinfo("Success", "Instructor deleted successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select an instructor to delete.")

    def list_instructors(self):
        self.clear_displayed_data()
        self.instructor_listbox.delete(0, tk.END)
        instructors = Instructor.get_instructors(self.db)
        if instructors:
            for instructor in instructors:
                self.instructors_displayed.append(instructor)
                instructor_info = f"ID: {instructor[0]}, Name: {instructor[1]}, Email: {instructor[2]}"
                self.instructor_listbox.insert(tk.END, instructor_info)
        else:
            self.instructor_listbox.insert(tk.END, "No instructors found.")

    def create_student_tab(self):
        student_tab = ttk.Frame(self.notebook)
        self.notebook.add(student_tab, text="Students")

        # Student Management UI elements
        tk.Label(student_tab, text="Student Management", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        tk.Label(student_tab, text="Student Name:").grid(row=1, column=0, padx=10, pady=5)
        self.student_name_entry = tk.Entry(student_tab)
        self.student_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(student_tab, text="Student Email:").grid(row=2, column=0, padx=10, pady=5)
        self.student_email_entry = tk.Entry(student_tab)
        self.student_email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        add_button = tk.Button(student_tab, text="Add Student", command=self.add_student)
        add_button.grid(row=3, column=0, padx=10, pady=10)

        update_button = tk.Button(student_tab, text="Update Student", command=self.update_student)
        update_button.grid(row=3, column=1, padx=10, pady=10)

        delete_button = tk.Button(student_tab, text="Delete Student", command=self.delete_student)
        delete_button.grid(row=3, column=2, padx=10, pady=10)

        list_button = tk.Button(student_tab, text="Refresh List", command=self.list_students)
        list_button.grid(row=3, column=3, padx=10, pady=10)

        # Listbox for displaying students
        self.student_listbox = tk.Listbox(student_tab, height=10, width=100)
        self.student_listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(student_tab, orient="vertical")
        scrollbar.config(command=self.student_listbox.yview)
        scrollbar.grid(row=4, column=4, sticky="ns")

        self.student_listbox.config(yscrollcommand=scrollbar.set)

    def add_student(self):
        student_name = self.student_name_entry.get()
        student_email = self.student_email_entry.get()
        try:
            Student.create_student(self.db, student_name, student_email)
            messagebox.showinfo("Success", "Student added successfully!")
            self.refresh_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        selected_student = self.student_listbox.curselection()
        if selected_student:
            student_id = self.students_displayed[selected_student[0]][0]
            student_name = self.student_name_entry.get()
            student_email = self.student_email_entry.get()
            try:
                Student.update_student(self.db, student_id, student_name, student_email)
                messagebox.showinfo("Success", "Student updated successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a student to update.")

    def delete_student(self):
        selected_student = self.student_listbox.curselection()
        if selected_student:
            student_id = self.students_displayed[selected_student[0]][0]
            try:
                Student.delete_student(self.db, student_id)
                messagebox.showinfo("Success", "Student deleted successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a student to delete.")

    def list_students(self):
        self.clear_displayed_data()
        self.student_listbox.delete(0, tk.END)
        students = Student.get_students(self.db)
        if students:
            for student in students:
                self.students_displayed.append(student)
                student_info = f"ID: {student[0]}, Name: {student[1]}, Email: {student[2]}"
                self.student_listbox.insert(tk.END, student_info)
        else:
            self.student_listbox.insert(tk.END, "No students found.")

    def create_assessment_tab(self):
        assessment_tab = ttk.Frame(self.notebook)
        self.notebook.add(assessment_tab, text="Assessments")

        # Assessment Management UI elements
        tk.Label(assessment_tab, text="Assessment Management", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        tk.Label(assessment_tab, text="Assessment Name:").grid(row=1, column=0, padx=10, pady=5)
        self.assessment_name_entry = tk.Entry(assessment_tab)
        self.assessment_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(assessment_tab, text="Assessment Description:").grid(row=2, column=0, padx=10, pady=5)
        self.assessment_description_entry = tk.Text(assessment_tab, height=5, width=30)
        self.assessment_description_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(assessment_tab, text="Assessment Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.assessment_date_entry = tk.Entry(assessment_tab)
        self.assessment_date_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        add_button = tk.Button(assessment_tab, text="Add Assessment", command=self.add_assessment)
        add_button.grid(row=4, column=0, padx=10, pady=10)

        update_button = tk.Button(assessment_tab, text="Update Assessment", command=self.update_assessment)
        update_button.grid(row=4, column=1, padx=10, pady=10)

        delete_button = tk.Button(assessment_tab, text="Delete Assessment", command=self.delete_assessment)
        delete_button.grid(row=4, column=2, padx=10, pady=10)

        list_button = tk.Button(assessment_tab, text="Refresh List", command=self.list_assessments)
        list_button.grid(row=4, column=3, padx=10, pady=10)

        # Listbox for displaying assessments
        self.assessment_listbox = tk.Listbox(assessment_tab, height=10, width=100)
        self.assessment_listbox.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(assessment_tab, orient="vertical")
        scrollbar.config(command=self.assessment_listbox.yview)
        scrollbar.grid(row=5, column=4, sticky="ns")

        self.assessment_listbox.config(yscrollcommand=scrollbar.set)

    def add_assessment(self):
        assessment_name = self.assessment_name_entry.get()
        assessment_description = self.assessment_description_entry.get("1.0", tk.END)
        assessment_date = self.assessment_date_entry.get()
        try:
            Assessment.create_assessment(self.db, assessment_name, assessment_description, assessment_date)
            messagebox.showinfo("Success", "Assessment added successfully!")
            self.refresh_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_assessment(self):
        selected_assessment = self.assessment_listbox.curselection()
        if selected_assessment:
            assessment_id = self.assessments_displayed[selected_assessment[0]][0]
            assessment_name = self.assessment_name_entry.get()
            assessment_description = self.assessment_description_entry.get("1.0", tk.END)
            assessment_date = self.assessment_date_entry.get()
            try:
                Assessment.update_assessment(self.db, assessment_id, assessment_name, assessment_description, assessment_date)
                messagebox.showinfo("Success", "Assessment updated successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select an assessment to update.")

    def delete_assessment(self):
        selected_assessment = self.assessment_listbox.curselection()
        if selected_assessment:
            assessment_id = self.assessments_displayed[selected_assessment[0]][0]
            try:
                Assessment.delete_assessment(self.db, assessment_id)
                messagebox.showinfo("Success", "Assessment deleted successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select an assessment to delete.")

    def list_assessments(self):
        self.clear_displayed_data()
        self.assessment_listbox.delete(0, tk.END)
        assessments = Assessment.get_assessments(self.db)
        if assessments:
            for assessment in assessments:
                self.assessments_displayed.append(assessment)
                assessment_info = f"ID: {assessment[0]}, Name: {assessment[1]}, Description: {assessment[2]}, Date: {assessment[3]}"
                self.assessment_listbox.insert(tk.END, assessment_info)
        else:
            self.assessment_listbox.insert(tk.END, "No assessments found.")

    def create_registration_tab(self):
        registration_tab = ttk.Frame(self.notebook)
        self.notebook.add(registration_tab, text="Registrations")

        # Registration Management UI elements
        tk.Label(registration_tab, text="Registration Management", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        tk.Label(registration_tab, text="Student ID:").grid(row=1, column=0, padx=10, pady=5)
        self.student_id_entry = tk.Entry(registration_tab)
        self.student_id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(registration_tab, text="Assessment ID:").grid(row=2, column=0, padx=10, pady=5)
        self.assessment_id_entry = tk.Entry(registration_tab)
        self.assessment_id_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(registration_tab, text="Registration Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.registration_date_entry = tk.Entry(registration_tab)
        self.registration_date_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        add_button = tk.Button(registration_tab, text="Add Registration", command=self.add_registration)
        add_button.grid(row=4, column=0, padx=10, pady=10)

        update_button = tk.Button(registration_tab, text="Update Registration", command=self.update_registration)
        update_button.grid(row=4, column=1, padx=10, pady=10)

        delete_button = tk.Button(registration_tab, text="Delete Registration", command=self.delete_registration)
        delete_button.grid(row=4, column=2, padx=10, pady=10)

        list_button = tk.Button(registration_tab, text="Refresh List", command=self.list_registrations)
        list_button.grid(row=4, column=3, padx=10, pady=10)

        # Listbox for displaying registrations
        self.registration_listbox = tk.Listbox(registration_tab, height=10, width=100)
        self.registration_listbox.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(registration_tab, orient="vertical")
        scrollbar.config(command=self.registration_listbox.yview)
        scrollbar.grid(row=5, column=4, sticky="ns")

        self.registration_listbox.config(yscrollcommand=scrollbar.set)

    def add_registration(self):
        student_id = self.student_id_entry.get()
        assessment_id = self.assessment_id_entry.get()
        registration_date = self.registration_date_entry.get()
        try:
            Registration.create_registration(self.db, student_id, assessment_id, registration_date)
            messagebox.showinfo("Success", "Registration added successfully!")
            self.refresh_display()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_registration(self):
        selected_registration = self.registration_listbox.curselection()
        if selected_registration:
            registration_id = self.registrations_displayed[selected_registration[0]][0]
            student_id = self.student_id_entry.get()
            assessment_id = self.assessment_id_entry.get()
            registration_date = self.registration_date_entry.get()
            try:
                Registration.update_registration(self.db, registration_id, student_id, assessment_id, registration_date)
                messagebox.showinfo("Success", "Registration updated successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a registration to update.")

    def delete_registration(self):
        selected_registration = self.registration_listbox.curselection()
        if selected_registration:
            registration_id = self.registrations_displayed[selected_registration[0]][0]
            try:
                Registration.delete_registration(self.db, registration_id)
                messagebox.showinfo("Success", "Registration deleted successfully!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please select a registration to delete.")

    def list_registrations(self):
        self.clear_displayed_data()
        self.registration_listbox.delete(0, tk.END)
        registrations = Registration.get_registrations(self.db)
        if registrations:
            for registration in registrations:
                self.registrations_displayed.append(registration)
                registration_info = f"ID: {registration[0]}, Student ID: {registration[1]}, Assessment ID: {registration[2]}, Registration Date: {registration[3]}"
                self.registration_listbox.insert(tk.END, registration_info)
        else:
            self.registration_listbox.insert(tk.END, "No registrations found.")

    def clear_displayed_data(self):
        self.instructors_displayed = []
        self.students_displayed = []
        self.assessments_displayed = []
        self.registrations_displayed = []

    def refresh_display(self):
        self.clear_displayed_data()
        self.list_instructors()
        self.list_students()
        self.list_assessments()
        self.list_registrations()

    def close(self):
        self.db.close()
        self.window.destroy()

def main():
    root = tk.Tk()
    app = EduSchemaApp(root)
    app.run()

if __name__ == "__main__":
    main()
