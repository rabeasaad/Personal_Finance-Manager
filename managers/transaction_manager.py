from models.transaction import Transaction, ExpenseTransaction, IncomeTransaction
from exceptions import ValidationError, NotFoundError
from datetime import datetime

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def list_transactions(self):
        if not self.transactions:
            print("No transactions found.\n")
        else:
            print("\nList of Transactions:")
            for t in self.transactions:
                print(f"ID: {t.id}, Account ID: {t.account_id}, Date: {t.date}, "
                      f"Amount: {t.amount}, Description: {t.description}, Category: {t.category}")
            print()

    def validate_date(self, date):
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValidationError("Invalid date format. Use YYYY-MM-DD.")

    def create_transaction(self, trans_id, account_id, date, amount, description, category, trans_type):

        for t in self.transactions:
            if t.id == trans_id:
                raise ValidationError("Transaction ID already exists.")

        self.validate_date(date)

        if amount < 0:
            raise ValidationError("Amount must be positive.")

        if trans_type.lower() == "expense":
            transaction = ExpenseTransaction(trans_id, account_id, date, amount, description, category)
        elif trans_type.lower() == "income":
            transaction = IncomeTransaction(trans_id, account_id, date, amount, description, category)
        else:
            raise ValidationError("Invalid transaction type. Use 'expense' or 'income'.")

        self.transactions.append(transaction)
        print("Transaction added successfully!\n")

    def delete_transaction(self, trans_id):
        for t in self.transactions:
            if t.id == trans_id:
                self.transactions.remove(t)
                print("Transaction deleted successfully!\n")
                return
        raise NotFoundError("Transaction not found.")

    def update_transaction(self, trans_id, **kwargs):
        transaction = next((t for t in self.transactions if t.id == trans_id), None)
        if not transaction:
            raise NotFoundError("Transaction not found.")

        if 'account_id' in kwargs:
            transaction.account_id = kwargs['account_id']
        if 'date' in kwargs:
            self.validate_date(kwargs['date'])
            transaction.date = kwargs['date']
        if 'amount' in kwargs:
            if kwargs['amount'] < 0:
                raise ValidationError("Amount must be positive.")
            transaction.amount = kwargs['amount']
        if 'description' in kwargs:
            transaction.description = kwargs['description']
        if 'category' in kwargs:
            transaction.category = kwargs['category']

        print("Transaction updated successfully!\n")
