import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO experts (name, email) VALUES (?, ?)",
            ('First Person', 'first@example.com')
            )

cur.execute("INSERT INTO experts (name, email) VALUES (?, ?)",
            ('Second Person', 'second@example.com')
            )

connection.commit()
connection.close()
