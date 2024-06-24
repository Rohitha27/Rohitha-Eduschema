# Rohitha-Eduschema

## Educational Management System

### Overview
This project is a Python-based educational management system designed to manage courses, instructors, students, assessments, and enrollments using a MySQL database backend. It provides a command-line interface (CLI) for interacting with the database and performing CRUD operations on the entities mentioned.

### Project Structure
The project consists of the following main components:

- **database.py**: Handles database connections and query execution.
- **main.py**: Main executable file providing the CLI interface for management operations.
- **models.py**: Defines Python classes for database entities with CRUD operations.
- **edu_schema.sql**: SQL script to create the MySQL database and tables.

### Functionality

#### Main Features
- **Course Management**: CRUD operations for courses.
- **Instructor Management**: CRUD operations for instructors.
- **Student Management**: CRUD operations for students.
- **Assessment Management**: CRUD operations for assessments.
- **Enrollment Management**: Operations to enroll, update enrollments, and withdraw students.
- **View Deleted Entries**: View soft-deleted records.

### Usage
#### Setting Up the Database
1. Execute `edu_schema.sql` to create the `edu_schema` database and necessary tables in your MySQL server.
2. Ensure MySQL server is running and accessible.

#### Python Environment Setup
- Install required Python packages using pip:

#### Running the Application
1. Execute `main.py` to start the CLI interface.
2. Follow the prompts to navigate through different management menus and perform desired operations.

#### Exiting the Application
- Use the exit option (7) from the main menu to close the application gracefully.

### Future Enhancements
- Implement authentication and access control for different user roles.
- Improve error handling and input validation.
- Add features such as grading management, reporting, and analytics.

### Dependencies
- Python 3.x
- mysql-connector-python (Python MySQL connector)
  
