from database import Database

class Course:
    def __init__(self, course_id, course_name, course_description, start_date, end_date):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def create_course(db, course_name, course_description, start_date, end_date):
        query = "INSERT INTO courses (course_name, course_description, start_date, end_date) VALUES (%s, %s, %s, %s)"
        db.execute_query(query, (course_name, course_description, start_date, end_date))

    @staticmethod
    def update_course(db, course_id, course_name, course_description, start_date, end_date):
        query = "UPDATE courses SET course_name=%s, course_description=%s, start_date=%s, end_date=%s WHERE course_id=%s"
        db.execute_query(query, (course_name, course_description, start_date, end_date, course_id))

    @staticmethod
    def delete_course(db, course_id):
        query = "UPDATE courses SET deleted=1 WHERE course_id=%s"
        db.execute_query(query, (course_id,))

    @staticmethod
    def get_courses(db):
        query = "SELECT * FROM courses WHERE deleted=0"
        return db.fetch_query(query)

    @staticmethod
    def get_deleted_courses(db):
        query = "SELECT * FROM courses WHERE deleted=1"
        return db.fetch_query(query)


class Instructor:
    def __init__(self, instructor_id, instructor_name, instructor_email):
        self.instructor_id = instructor_id
        self.instructor_name = instructor_name
        self.instructor_email = instructor_email

    @staticmethod
    def create_instructor(db, instructor_name, instructor_email):
        query = "INSERT INTO instructors (instructor_name, instructor_email) VALUES (%s, %s)"
        db.execute_query(query, (instructor_name, instructor_email))

    @staticmethod
    def update_instructor(db, instructor_id, instructor_name, instructor_email):
        query = "UPDATE instructors SET instructor_name=%s, instructor_email=%s WHERE instructor_id=%s"
        db.execute_query(query, (instructor_name, instructor_email, instructor_id))

    @staticmethod
    def delete_instructor(db, instructor_id):
        query = "UPDATE instructors SET deleted=1 WHERE instructor_id=%s"
        db.execute_query(query, (instructor_id,))

    @staticmethod
    def get_instructors(db):
        query = "SELECT * FROM instructors WHERE deleted=0"
        return db.fetch_query(query)

    @staticmethod
    def get_deleted_instructors(db):
        query = "SELECT * FROM instructors WHERE deleted=1"
        return db.fetch_query(query)


class Student:
    def __init__(self, student_id, student_name, student_email):
        self.student_id = student_id
        self.student_name = student_name
        self.student_email = student_email

    @staticmethod
    def create_student(db, student_name, student_email):
        query = "INSERT INTO students (student_name, student_email) VALUES (%s, %s)"
        db.execute_query(query, (student_name, student_email))

    @staticmethod
    def update_student(db, student_id, student_name, student_email):
        query = "UPDATE students SET student_name=%s, student_email=%s WHERE student_id=%s"
        db.execute_query(query, (student_name, student_email, student_id))

    @staticmethod
    def delete_student(db, student_id):
        query = "UPDATE students SET deleted=1 WHERE student_id=%s"
        db.execute_query(query, (student_id,))

    @staticmethod
    def get_students(db):
        query = "SELECT * FROM students WHERE deleted=0"
        return db.fetch_query(query)

    @staticmethod
    def get_deleted_students(db):
        query = "SELECT * FROM students WHERE deleted=1"
        return db.fetch_query(query)


class Assessment:
    def __init__(self, assessment_id, course_id, assessment_name, assessment_date):
        self.assessment_id = assessment_id
        self.course_id = course_id
        self.assessment_name = assessment_name
        self.assessment_date = assessment_date

    @staticmethod
    def create_assessment(db, course_id, assessment_name, assessment_date):
        query = "INSERT INTO assessments (course_id, assessment_name, assessment_date) VALUES (%s, %s, %s)"
        db.execute_query(query, (course_id, assessment_name, assessment_date))

    @staticmethod
    def update_assessment(db, assessment_id, course_id, assessment_name, assessment_date):
        query = "UPDATE assessments SET course_id=%s, assessment_name=%s, assessment_date=%s WHERE assessment_id=%s"
        db.execute_query(query, (course_id, assessment_name, assessment_date, assessment_id))

    @staticmethod
    def delete_assessment(db, assessment_id):
        query = "UPDATE assessments SET deleted=1 WHERE assessment_id=%s"
        db.execute_query(query, (assessment_id,))

    @staticmethod
    def get_assessments_by_course(db, course_id):
        query = "SELECT * FROM assessments WHERE course_id=%s AND deleted=0"
        return db.fetch_query(query, (course_id,))

    @staticmethod
    def get_deleted_assessments(db):
        query = "SELECT * FROM assessments WHERE deleted=1"
        return db.fetch_query(query)


class Grade:
    def __init__(self, grade_id, student_id, assessment_id, grade):
        self.grade_id = grade_id
        self.student_id = student_id
        self.assessment_id = assessment_id
        self.grade = grade

    @staticmethod
    def create_grade(db, student_id, assessment_id, grade):
        query = "INSERT INTO grades (student_id, assessment_id, grade) VALUES (%s, %s, %s)"
        db.execute_query(query, (student_id, assessment_id, grade))

    @staticmethod
    def update_grade(db, grade_id, student_id, assessment_id, grade):
        query = "UPDATE grades SET student_id=%s, assessment_id=%s, grade=%s WHERE grade_id=%s"
        db.execute_query(query, (student_id, assessment_id, grade, grade_id))

    @staticmethod
    def delete_grade(db, grade_id):
        query = "UPDATE grades SET deleted=1 WHERE grade_id=%s"
        db.execute_query(query, (grade_id,))

    @staticmethod
    def get_grades_by_student(db, student_id):
        query = "SELECT * FROM grades WHERE student_id=%s AND deleted=0"
        return db.fetch_query(query, (student_id,))

    @staticmethod
    def get_grades_by_assessment(db, assessment_id):
        query = "SELECT * FROM grades WHERE assessment_id=%s AND deleted=0"
        return db.fetch_query(query, (assessment_id,))

    @staticmethod
    def get_deleted_grades(db):
        query = "SELECT * FROM grades WHERE deleted=1"
        return db.fetch_query(query)


class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id, enrollment_date, completion_status):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date
        self.completion_status = completion_status

    @staticmethod
    def enroll_student(db, student_id, course_id, enrollment_date, completion_status='In Progress'):
        query = "INSERT INTO enrollments (student_id, course_id, enrollment_date, completion_status) VALUES (%s, %s, %s, %s)"
        db.execute_query(query, (student_id, course_id, enrollment_date, completion_status))

    @staticmethod
    def update_enrollment(db, enrollment_id, student_id, course_id, enrollment_date, completion_status):
        query = "UPDATE enrollments SET student_id=%s, course_id=%s, enrollment_date=%s, completion_status=%s WHERE enrollment_id=%s"
        db.execute_query(query, (student_id, course_id, enrollment_date, completion_status, enrollment_id))

    @staticmethod
    def delete_enrollment(db, enrollment_id):
        query = "UPDATE enrollments SET deleted=1 WHERE enrollment_id=%s"
        db.execute_query(query, (enrollment_id,))

    @staticmethod
    def get_enrollments_by_student(db, student_id):
        query = "SELECT * FROM enrollments WHERE student_id=%s AND deleted=0"
        return db.fetch_query(query, (student_id,))

    @staticmethod
    def get_enrollments_by_course(db, course_id):
        query = "SELECT * FROM enrollments WHERE course_id=%s AND deleted=0"
        return db.fetch_query(query, (course_id,))

    @staticmethod
    def get_deleted_enrollments(db):
        query = "SELECT * FROM enrollments WHERE deleted=1"
        return db.fetch_query(query)
