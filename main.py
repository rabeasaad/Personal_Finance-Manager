from managers.account_manager import AccountManager
from managers.transaction_manager import TransactionManager
from managers.budget_manager import BudgetManager
from storage.csv_storage import save_to_csv, load_from_csv
from models.account import CashAccount, BankAccount
from models.transaction import ExpenseTransaction, IncomeTransaction
from models.budget import Budget
from exceptions import FinanceError

account_manager = AccountManager()
transaction_manager = TransactionManager()
budget_manager = BudgetManager()


def initialize_csv_files():
    load_from_csv("accounts.csv", account_manager.accounts, cls=CashAccount)
    load_from_csv("transactions.csv", transaction_manager.transactions, cls=ExpenseTransaction)
    load_from_csv("budgets.csv", budget_manager.budgets, cls=Budget)


def accounts_menu():
    while True:
        print("Accounts Menu: 1. List | 2. Create | 3. Update | 4. Delete | 5. Back")
        choice = input("Choose: ")
        try:
            if choice == '1':
                account_manager.list_accounts()
            elif choice == '2':
                acc_id = input("Enter account ID: ")
                name = input("Enter account name: ")
                acc_type = input("Enter type (cash/bank): ")
                currency = input("Enter currency: ")
                account_manager.create_account(acc_id, name, acc_type, currency)
            elif choice == '3':
                acc_id = input("Enter account ID to update: ")
                name = input("New name (or leave empty): ")
                acc_type = input("New type (or leave empty): ")
                currency = input("New currency (or leave empty): ")
                account_manager.update_account(acc_id, name, acc_type, currency)
            elif choice == '4':
                acc_id = input("Enter account ID to delete: ")
                account_manager.delete_account(acc_id)
            elif choice == '5':
                break
            else:
                print("Invalid choice!\n")
        except FinanceError as e:
            print(f"Error: {e}\n")

def transactions_menu():
    while True:
        print("Transactions Menu: 1. List | 2. Create | 3. Update | 4. Delete | 5. Back")
        choice = input("Choose: ")
        try:
            if choice == '1':
                transaction_manager.list_transactions()
            elif choice == '2':
                trans_id = input("Enter transaction ID: ")
                account_id = input("Enter account ID: ")
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                trans_type = input("Enter type (expense/income): ")
                transaction_manager.create_transaction(trans_id, account_id, date, amount, description, category, trans_type)

            elif choice == '3':  # Update
                trans_id = input("Enter transaction ID to update: ")
                print("Enter new values (leave blank to skip):")
                new_desc = input("New description: ")
                new_amount = input("New amount: ")
                new_category = input("New category: ")
                new_date = input("New date (YYYY-MM-DD): ")

                updates = {}
                if new_desc:
                    updates['description'] = new_desc
                if new_amount:
                    updates['amount'] = float(new_amount)
                if new_category:
                    updates['category'] = new_category
                if new_date:
                    updates['date'] = new_date

                transaction_manager.update_transaction(trans_id, **updates)

            elif choice == '4':
                trans_id = input("Enter transaction ID to delete: ")
                transaction_manager.delete_transaction(trans_id)
            elif choice == '5':
                break
            else:
                print("Invalid choice!\n")

        except FinanceError as e:
            print(f"Error: {e}\n")
        except ValueError:
            print("Invalid input. Amount must be a number.\n")


def budgets_menu():
    while True:
        print("Budgets Menu: 1. List | 2. Create | 3. Update | 4. Delete | 5. Back")
        choice = input("Choose: ")
        try:
            if choice == '1':
                budget_manager.list_budgets()
            elif choice == '2':
                b_id = input("Enter budget ID: ")
                month = input("Enter month (YYYY-MM): ")
                category = input("Enter category: ")
                limit_amount = float(input("Enter limit amount: "))
                budget_manager.create_budget(b_id, month, category, limit_amount)
            elif choice == '3':
                b_id = input("Enter budget ID to update: ")
                month = input("New month (or leave empty): ")
                category = input("New category (or leave empty): ")
                limit = input("New limit amount (or leave empty): ")
                limit_amount = float(limit) if limit else None
                budget_manager.update_budget(b_id, month, category, limit_amount)
            elif choice == '4':
                b_id = input("Enter budget ID to delete: ")
                budget_manager.delete_budget(b_id)
            elif choice == '5':
                break
            else:
                print("Invalid choice!\n")
        except FinanceError as e:
            print(f"Error: {e}\n")
        except ValueError:
            print("Invalid limit amount. Must be a number.\n")


def save_all():
    save_to_csv("accounts.csv", account_manager.accounts, ["id", "name", "type", "currency"])
    save_to_csv("transactions.csv", transaction_manager.transactions, ["id", "account_id", "date", "amount", "description", "category"])
    save_to_csv("budgets.csv", budget_manager.budgets, ["id", "month", "category", "limit_amount"])
    print("All data saved successfully!\n")

def load_all():
    initialize_csv_files()   
    print("All data loaded successfully!\n")  
    #input("Press Enter to return to the main menu...") 

def main_menu():
    initialize_csv_files()
    while True:
        print("=== Personal Finance Manager ===")
        print("1. Manage Accounts")
        print("2. Manage Transactions")
        print("3. Manage Budgets")
        print("4. Save all to CSV")
        print("5. Load all from CSV")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            accounts_menu()
        elif choice == '2':
            transactions_menu()
        elif choice == '3':
            budgets_menu()
        elif choice == '4':
            save_all()
        elif choice == '5':
            load_all()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main_menu()
