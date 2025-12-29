from models.account import Account, CashAccount, BankAccount
from exceptions import ValidationError, NotFoundError

class AccountManager:
    VALID_CURRENCIES = ["HUF", "USD", "EUR"]

    def __init__(self):
        self.accounts = []

    def list_accounts(self):
        if not self.accounts:
            print("No accounts found.\n")
        else:
            print("\nList of Accounts:")
            for acc in self.accounts:
                print(f"ID: {acc.id}, Name: {acc.name}, Type: {acc.type}, Currency: {acc.currency}")
            print()

    def create_account(self, acc_id, name, acc_type, currency):
        
        for acc in self.accounts:
            if acc.id == acc_id:
                raise ValidationError("Account ID already exists.")

        
        acc_type = acc_type.lower()
        if acc_type not in ["cash", "bank"]:
            raise ValidationError("Invalid account type. Use 'cash' or 'bank'.")

        
        if currency not in self.VALID_CURRENCIES:
            raise ValidationError(f"Invalid currency. Choose from {self.VALID_CURRENCIES}.")

        if acc_type == "cash":
            account = CashAccount(acc_id, name, currency)
        else:
            account = BankAccount(acc_id, name, currency)

        self.accounts.append(account)
        print("Account created successfully!\n")

    def update_account(self, acc_id, name=None, acc_type=None, currency=None):
        for acc in self.accounts:
            if acc.id == acc_id:
                if name:
                    acc.name = name
                if currency:
                    if currency not in self.VALID_CURRENCIES:
                        raise ValidationError(f"Invalid currency. Choose from {self.VALID_CURRENCIES}.")
                    acc.currency = currency
                if acc_type:
                    acc_type = acc_type.lower()
                    if acc_type not in ["cash", "bank"]:
                        raise ValidationError("Invalid account type. Use 'cash' or 'bank'.")
                    acc.type = acc_type
                print("Account updated successfully!\n")
                return
        raise NotFoundError("Account not found.")

    def delete_account(self, acc_id):
        for acc in self.accounts:
            if acc.id == acc_id:
                self.accounts.remove(acc)
                print("Account deleted successfully!\n")
                return
        raise NotFoundError("Account not found.")
