class Budget:
    def __init__(self, id, month, category, limit_amount):
        self.id = id
        self.month = month
        self.category = category
        self.limit_amount = float(limit_amount)
