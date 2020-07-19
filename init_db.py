import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO experts (name, curl) VALUES (?, ?)",
            ('First Person', '5a')
            )

cur.execute("INSERT INTO experts (name, curl) VALUES (?, ?)",
            ('Second Person', '1b')
            )

connection.commit()
connection.close()
