from models.budget import Budget
from exceptions import ValidationError, NotFoundError

class BudgetManager:
    def __init__(self):
        self.budgets = []

    def list_budgets(self):
        if not self.budgets:
            print("No budgets found.\n")
        else:
            print("\nList of Budgets:")
            for b in self.budgets:
                print(f"ID: {b.id}, Month: {b.month}, Category: {b.category}, Limit Amount: {b.limit_amount}")
            print()

    def validate_month(self, month):
        
        import re
        if not re.match(r"^\d{4}-(0[1-9]|1[0-2])$", month):
            raise ValidationError("Invalid month format. Use YYYY-MM.")

    def create_budget(self, budget_id, month, category, limit_amount):
        
        for b in self.budgets:
            if b.id == budget_id:
                raise ValidationError("Budget ID already exists.")

        self.validate_month(month)

        if limit_amount < 0:
            raise ValidationError("Limit amount must be positive.")

        budget = Budget(budget_id, month, category, limit_amount)
        self.budgets.append(budget)
        print("Budget created successfully!\n")

    def update_budget(self, budget_id, month=None, category=None, limit_amount=None):
        for b in self.budgets:
            if b.id == budget_id:
                if month: 
                    self.validate_month(month)
                    b.month = month
                if category:
                    b.category = category
                if limit_amount is not None:
                    if limit_amount < 0:
                        raise ValidationError("Limit amount must be positive.")
                    b.limit_amount = limit_amount
                print("Budget updated successfully!\n")
                return
        raise NotFoundError("Budget not found.")

    def delete_budget(self, budget_id):
        for b in self.budgets:
            if b.id == budget_id:
                self.budgets.remove(b)
                print("Budget deleted successfully!\n")
                return
        raise NotFoundError("Budget not found.")
