import sqlite3
import shutil

def init_db():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        amount REAL,
        category TEXT,
        type TEXT,  -- 'income' or 'expense'
        date TEXT
    )
    """)

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS budgets ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT, 
        category TEXT, 
        amount REAL 
        ) 
        """) 
    conn.commit() 
    conn.close()

# Existing functions for user management
def save_user(username, password):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Username already exists.")
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def backup_database(): 
    try: 
        shutil.copyfile("finance.db", "finance_backup.db") 
        print("Backup created successfully!") 
    except Exception as e: 
        print(f"Error creating backup: {e}") 
        
def restore_database(): 
    try: 
        shutil.copyfile("finance_backup.db", "finance.db") 
        print("Database restored successfully!") 
    except Exception as e: 
        print(f"Error restoring database: {e}")
