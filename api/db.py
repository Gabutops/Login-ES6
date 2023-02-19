import sqlite3

db = sqlite3.connect("my_database.db")
db.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY,
              username TEXT,
              email TEXT,
              password TEXT)''')
        