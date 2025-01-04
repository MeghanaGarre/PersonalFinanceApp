import sqlite3

def set_budget(username, category, amount):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO budgets (username, category, amount)
    VALUES (?, ?, ?)
    """, (username, category, amount))
    conn.commit()
    conn.close()

def get_budget(username, category):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM budgets WHERE username = ? AND category = ?", (username, category))
    budget = cursor.fetchone()
    conn.close()
    return budget[0] if budget else None

def check_budget(username, category):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT SUM(amount) FROM transactions
    WHERE username = ? AND category = ? AND type = 'expense'
    """, (username, category))
    total_expenses = cursor.fetchone()[0] or 0
    budget = get_budget(username, category)
    conn.close()
    
    if budget is not None and total_expenses > budget:
        return f"Warning: You have exceeded your budget for {category}. Budget: {budget}, Expenses: {total_expenses}"
    elif budget is not None:
        return f"Budget for {category}: {budget}, Expenses: {total_expenses}. You are within your budget."
    else:
        return "No budget set for this category."

def view_budgets(username):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budgets WHERE username = ?", (username,))
    budgets = cursor.fetchall()
    conn.close()
    return budgets
