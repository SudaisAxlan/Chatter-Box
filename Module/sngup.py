from flask import Flask,request,jsonify
import sqlite3
from flask_mail import Mail, Message
# mail = None


def userRegister():

    if request.method == "POST":
        # Get JSON data from the request
        data = request.get_json()

        # Extract username, email, and password from the JSON data
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Connect to SQLite database (or create it if it doesn't exist)
        
        conn = sqlite3.connect('ChatingApp.db')
        c = conn.cursor()

        # Create the table if it doesn't already exist
        # c.execute("SELECT * FROM new_user WHERE username = ? AND password = ?",(username,password))
            
        
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS new_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        c.execute('''
            SELECT * FROM new_user WHERE username = ? OR email = ?
        ''', (username, email))
         
        existing_user = c.fetchone()
        if existing_user:
                # If user exists, return an error message
            conn.close()
            return jsonify({"Email or Username are alredy exit.."}), 409


        # Insert user data from the request
        c.execute('''
            INSERT INTO new_user(username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, password))

        # Commit changes and close the connection
        conn.commit()
        conn.close()


        # Return a success message
        return jsonify({"message": "User successfully registered!"}), 200

    return jsonify({"error": "Invalid request method. Use POST."}), 400