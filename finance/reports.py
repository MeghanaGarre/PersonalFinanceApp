import sqlite3

def generate_monthly_report(username, month, year):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT type, SUM(amount) 
    FROM transactions 
    WHERE username = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ? 
    GROUP BY type
    """, (username, f'{month:02}', str(year)))
    
    report = cursor.fetchall()
    conn.close()
    
    income = sum([row[1] for row in report if row[0] == 'income'])
    expenses = sum([row[1] for row in report if row[0] == 'expense'])
    savings = income - expenses
    
    print(f"Monthly Report for {month}/{year}:")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Total Savings: {savings}")
    
    return income, expenses, savings

def generate_yearly_report(username, year):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT type, SUM(amount) 
    FROM transactions 
    WHERE username = ? AND strftime('%Y', date) = ? 
    GROUP BY type
    """, (username, str(year)))
    
    report = cursor.fetchall()
    conn.close()
    
    income = sum([row[1] for row in report if row[0] == 'income'])
    expenses = sum([row[1] for row in report if row[0] == 'expense'])
    savings = income - expenses
    
    print(f"Yearly Report for {year}:")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Total Savings: {savings}")
    
    return income, expenses, savings
