import sqlite3
from datetime import datetime

def add_transaction(username, amount, category, transaction_type):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    INSERT INTO transactions (username, amount, category, type, date)
    VALUES (?, ?, ?, ?, ?)
    """, (username, amount, category, transaction_type, date))
    conn.commit()
    conn.close()

def update_transaction(transaction_id, amount, category, transaction_type):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE transactions
    SET amount = ?, category = ?, type = ?
    WHERE id = ?
    """, (amount, category, transaction_type, transaction_id))
    conn.commit()
    conn.close()

def delete_transaction(transaction_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()

def view_transactions(username):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE username = ?", (username,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions
