

class Account:
    def __init__(self, id, name, type, currency):
        self.id = id
        self.name = name
        self.type = type
        self.currency = currency

class CashAccount(Account):
    def __init__(self, id, name, currency):
        super().__init__(id, name, "cash", currency)

class BankAccount(Account):
    def __init__(self, id, name, currency):
        super().__init__(id, name, "bank", currency)
