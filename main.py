import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

def create_user(name, age):
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def read_users():
    c.execute("SELECT * FROM users")
    return c.fetchall()

def update_user(id, name, age):
    c.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()

def delete_user(id):
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()

create_user('John Doe', 30)
create_user('Jane Doe', 25)

print(read_users())

update_user(1, 'John Smith', 31)

print(read_users())

delete_user(2)

print(read_users())

conn.close()