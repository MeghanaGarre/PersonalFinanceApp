import bcrypt
from db.database import get_user_by_username

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = get_user_by_username(username)
    if user:
        stored_hash = user[2]  # Assuming the third column is the hashed password
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print("Login successful!")
            return username
        else:
            print("Incorrect password.")
            return None
    else:
        print("Username not found.")
        return None
