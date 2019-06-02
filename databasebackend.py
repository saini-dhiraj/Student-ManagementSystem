import sqlite3

connection = sqlite3.connect('student.db')
print("Database open")

table_name = "student_table"
student_id = "student_id"
student_name = "student_name"
student_college = "student_college"
student_address = "student_address"
student_phone = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + table_name + " ( " + student_id +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   student_name + " TEXT, " + student_college + " TEXT, "
                   + student_address + " TEXT, " + student_phone
                   + " INTEGER);")

# SQLITE QUERY: CREATE TABLE IF NOT EXISTS student_table(student_id INTEGER PRIMARY KEY AUTOINCREMENT,
# student_name TEXT,student_college TEXT)

print("Table created successfully")


def display():
    cursor = connection.execute("SELECT * FROM " + table_name + " ;")
    return cursor


def insert(name,college,address,phone):
    connection.execute("INSERT INTO " + table_name + " ( " + student_name + ", " + student_college + ", " +
                        student_address + ", " + student_phone +
                        ") VALUES ('"+name+"','"+college+"','"+address+"',"+phone+")")
    connection.commit()
    return True
