from auth.registration import register_user
from auth.login import login_user
from db.database import init_db, backup_database, restore_database
from finance.transactions import add_transaction, update_transaction, delete_transaction, view_transactions
from finance.reports import generate_monthly_report, generate_yearly_report
from finance.budgeting import set_budget, get_budget, check_budget, view_budgets
from datetime import datetime

def main():
    init_db()
    print("Welcome to Personal Finance App")
    
    while True:
        choice = input("1. Register\n2. Login\n3. Backup Database\n4. Restore Database\n5. Exit\nChoose an option: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                print(f"Login successful! Welcome {username}")
                while True:
                    transaction_choice = input("1. Add Transaction\n2. Update Transaction\n3. Delete Transaction\n4. View Transactions\n5. Generate Monthly Report\n6. Generate Yearly Report\n7. Set Budget\n8. Check Budget\n9. View Budgets\n10. Logout\nChoose an option: ")
                    if transaction_choice == "1":
                        username=input("Enter username: ")
                        amount = float(input("Enter amount: "))
                        category = input("Enter category (e.g., Salary, Rent, Food): ")
                        transaction_type = input("Enter type (income/expense): ").lower()
                        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        while transaction_type not in ['income', 'expense']:
                            print("Invalid input. Please enter 'income' or 'expense'.")
                            transaction_type = input("Enter type (income/expense): ").lower()
                        add_transaction(username, amount, category, transaction_type, date)
                        print("Transaction added successfully!")
                    elif transaction_choice == "2":
                        transaction_id = int(input("Enter transaction ID to update: "))
                        amount = float(input("Enter new amount: "))
                        category = input("Enter new category (e.g., Salary, Rent, Food): ")
                        transaction_type = input("Enter new type (income/expense): ").lower()
                        update_transaction(transaction_id, amount, category, transaction_type)
                        print("Transaction updated successfully!")
                    elif transaction_choice == "3":
                        transaction_id = int(input("Enter transaction ID to delete: "))
                        delete_transaction(transaction_id)
                        print("Transaction deleted successfully!")
                    elif transaction_choice == "4":
                        transactions = view_transactions(username)
                        if transactions:
                            for transaction in transactions:
                                print(transaction)
                        else:
                            print("No transactions found.")
                    elif transaction_choice == "5":
                        month = int(input("Enter month (1-12): "))
                        year = int(input("Enter year (e.g., 2025): "))
                        generate_monthly_report(username, month, year)
                    elif transaction_choice == "6":
                        year = int(input("Enter year (e.g., 2025): "))
                        generate_yearly_report(username, year)
                    elif transaction_choice == "7":
                        category = input("Enter category (e.g., Salary, Rent, Food): ")
                        amount = float(input("Enter budget amount: "))
                        set_budget(username, category, amount)
                        print("Budget set successfully!")
                    elif transaction_choice == "8":
                        category = input("Enter category to check budget (e.g., Salary, Rent, Food): ")
                        result = check_budget(username, category)
                        print(result)
                    elif transaction_choice == "9":
                        budgets = view_budgets(username)
                        if budgets:
                            for budget in budgets:
                                print(budget)
                        else:
                            print("No budgets found.")
                    elif transaction_choice == "10":
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please check your username and password.")
        elif choice == "3":
            backup_database()
        elif choice == "4":
            restore_database()
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
