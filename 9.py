import sqlite3

# Function to establish a connection to the SQLite database
def connect_db():
    try:
        conn = sqlite3.connect('student_management.db')
        return conn
    except sqlite3.Error as e:
        print("Database connection error:", e)
        return None

# Function to create the student table
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
        ''')
        conn.commit()
        print("Student table created successfully.")
    except sqlite3.Error as e:
        print("Error creating table:", e)

# Function to add a new student
def add_student(conn, student_id, name, age, grade): 
    try:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO students (id, name, age, grade) 
        VALUES (?, ?, ?, ?)
        ''', (student_id, name, age, grade))
        conn.commit()
        print("Student added successfully.")
    except sqlite3.Error as e:
        print("Error adding student:", e)

# Function to update a student record
def update_student(conn, student_id, name, age, grade): 
    try:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE students
        SET name = ?, age = ?, grade = ?
        WHERE id = ?
        ''', (name, age, grade, student_id))
        conn.commit()
        print("Student updated successfully.")
    except sqlite3.Error as e:
        print("Error updating student:", e)

# Function to delete a student record 
def delete_student(conn, student_id): 
    try:
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM students WHERE id = ?
        ''', (student_id,))
        conn.commit()
        print("Student deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting student:", e)

# Function to display all students 
def display_students(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        if students:
            print("\nStudent List:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        else:
            print("No students found.")
    except sqlite3.Error as e:
        print("Error fetching students:", e)

# Function to search for students by criteria 
def search_students(conn, criteria, value):
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM students WHERE {criteria} = ?', (value,))
        students = cursor.fetchall()
        if students:
            print("\nSearch Results:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        else:
            print("No matching students found.")
    except sqlite3.Error as e:
        print("Error searching students:", e)

# Main function to run the student management system 
def main():
    conn = connect_db()
    if conn is not None:
        create_table(conn)
        
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. Display All Students")
            print("5. Search Students")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = int(input("Enter student ID: ")) 
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                grade = input("Enter student grade: ")
                add_student(conn, student_id, name, age, grade)

            elif choice == '2':
                student_id = int(input("Enter student ID to update: ")) 
                name = input("Enter new name: ")
                age = int(input("Enter new age: ")) 
                grade = input("Enter new grade: ")
                update_student(conn, student_id, name, age, grade)

            elif choice == '3':
                student_id = int(input("Enter student ID to delete: ")) 
                delete_student(conn, student_id)

            elif choice == '4':
                display_students(conn)

            elif choice == '5':
                print("Search by: 1. ID 2. Name 3. Age 4. Grade") 
                search_choice = input("Enter your choice: ")

                if search_choice == '1': 
                    criteria = 'id'
                    value = int(input("Enter ID: ")) 
                elif search_choice == '2': 
                    criteria = 'name'
                    value = input("Enter name: ") 
                elif search_choice == '3': 
                    criteria = 'age'
                    value = int(input("Enter age: ")) 
                elif search_choice == '4': 
                    criteria = 'grade'
                    value = input("Enter grade: ")
                else:
                    print("Invalid choice.")
                    continue

                search_students(conn, criteria, value)

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        conn.close()

# Run the program
if __name__ == "__main__": 
    main()
