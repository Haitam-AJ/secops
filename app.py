import hashlib
import sqlite3

# Vulnerability 1: Use of a weak hash function
password = "password123"
md5_hash = hashlib.md5(password.encode()).hexdigest()

# Vulnerability 2: Use of exec function
user_input = input("Enter a command to execute: ")
exec(user_input)

# Vulnerability 3: SQL Injection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
user_id = 1
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
