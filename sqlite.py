import sqlite3

# connett to SQLite database
connection = sqlite3.connect('sqlchat.db')
cursor = connection.cursor()

# create table 

table_info = """
create table if not exists STUDENT (
    Name varchar(100),
    Class varchar(30),
    Section varchar(10),
    Marks int
);

"""

cursor.execute(table_info)

cursor.executemany("insert into STUDENT values (?,?,?,?)", [
    ('Alice', '10th', 'A', 85),
    ('Bob', '10th', 'B', 90),
    ('Charlie', '9th', 'A', 78),
    ('David', '9th', 'C', 88)
])


# Display all records
data = cursor.execute("select * from STUDENT").fetchall()
for row in data:
    print(row)


# commit changes and close connection
connection.commit()
connection.close()