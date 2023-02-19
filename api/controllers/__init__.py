import sqlite3
import json
import random
import string
from flask import jsonify
class controller(object):

    def insert_user(name, email, password):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        if not controller.check_email_exists(email):
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            return {
                    "Mensagem":"Login Efetuado com sucesso!",
                    "Status": 200
                    }
        else:
            return {
                "mensagem": "Email ja cadastrado",
                "Status": 200
            }
    def populate(n):
        for i in range(n):
        # Generate a random name
            first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
            last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
            name = f"{random.choice(first_names)} {random.choice(last_names)}"

            # Generate a random email
            email = f"{name.lower().replace(' ', '.')}@example.com"

            # Generate a random password
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

            # Insert the user into the database
            controller.insert_user(name, email, password)
        msg = {
            "Mensagem" : "Concluido",
            "Codigo":200
        }
        return msg

    def check_email_exists(email):
        # Connect to the database
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        # Check if the username or email already exists in the database
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()

        # Close the database connection
        conn.close()

        # Return True if the user or email already exists, False otherwise
        if result is not None:
            return True
        else:
            return False
    def get_users():
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        result = cursor.fetchall()
        users = []
        for row in result:
            user = {
                'id': row[0],
                'username': row[1],
                'email': row[2]
            }
            users.append(user)
        return jsonify(users)
        
    def get_all_users_json():
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM users")
        # Convert the list of tuples to a list of dictionaries
        users_json = []
        for user in users:
            user_json = {
                "id": user[0],
                "username": user[1],
                "email": user[2],
                "password": user[3]
            }
            users_json.append(user_json)
        return users_json