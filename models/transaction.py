
class Transaction:
    def __init__(self, trans_id, account_id, date, amount, description, category):
        self.id = trans_id
        self.account_id = account_id
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category

class ExpenseTransaction(Transaction):
    def __init__(self, trans_id, account_id, date, amount, description, category):
        super().__init__(trans_id, account_id, date, -abs(amount), description, category)

class IncomeTransaction(Transaction):
    def __init__(self, trans_id, account_id, date, amount, description, category):
        super().__init__(trans_id, account_id, date, abs(amount), description, category)
