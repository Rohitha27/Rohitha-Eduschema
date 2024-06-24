CREATE DATABASE edu_schema;
USE edu_schema;

-- Table: courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT,
    start_date DATE,
    end_date DATE
);

-- Table: instructors
CREATE TABLE instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    instructor_name VARCHAR(100) NOT NULL,
    instructor_email VARCHAR(100) UNIQUE
);

-- Table: course_instructors (to manage many-to-many relationship between courses and instructors)
CREATE TABLE course_instructors (
    course_id INT,
    instructor_id INT,
    PRIMARY KEY (course_id, instructor_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Table: students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    student_email VARCHAR(100) UNIQUE
);

-- Table: assessments
CREATE TABLE assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    assessment_name VARCHAR(100) NOT NULL,
    assessment_date DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Table: grades (to store grades for assessments)
CREATE TABLE grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    assessment_id INT,
    grade DECIMAL(5,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id)
);

-- Table: enrollments (to manage many-to-many relationship between students and courses)
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    completion_status ENUM('In Progress', 'Completed') DEFAULT 'In Progress',
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
SELECT * FROM Courses;
ALTER TABLE courses ADD COLUMN deleted TINYINT(1) DEFAULT 0;
ALTER TABLE instructors ADD COLUMN deleted TINYINT(1) DEFAULT 0;
ALTER TABLE students ADD COLUMN deleted TINYINT(1) DEFAULT 0;
ALTER TABLE assessments ADD COLUMN deleted TINYINT(1) DEFAULT 0;
ALTER TABLE enrollments ADD COLUMN deleted TINYINT(1) DEFAULT 0;

