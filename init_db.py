import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO experts (name, email, curl, length, density, porosity, oily, colored, permed, keratin, washMethod) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            ('Kelly', 'klf16@my.fsu.edu', '1a', 'long', "high", "high", "oily", "n", "n", "n", "What's going on here? I guess this is my washing method. Fun stuff."))

connection.commit()
connection.close()
