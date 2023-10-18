import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('user_database.db')
cursor = connection.cursor()

# Create the "users" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
''')

# Insert some sample data
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user1", "password1"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("user2", "password2"))

# Commit changes and close the database connection
connection.commit()
connection.close()
