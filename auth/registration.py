import bcrypt
from db.database import save_user

def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    save_user(username, hashed)
    print("User registered successfully!")
