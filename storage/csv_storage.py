
import os
import csv
from exceptions import StorageError
from models.account import CashAccount, BankAccount
from models.transaction import ExpenseTransaction, IncomeTransaction

def save_to_csv(filename, data, fieldnames):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(vars(item))
    except Exception as e:
        raise StorageError(f"Error saving to CSV: {e}")

def load_from_csv(filename, cls_list, cls=None):

    
    if not os.path.exists(filename):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            if cls in [CashAccount, BankAccount]:
                writer = csv.writer(csvfile)
                writer.writerow(['id', 'name', 'currency'])
            elif cls in [ExpenseTransaction, IncomeTransaction]:
                writer = csv.writer(csvfile)
                writer.writerow(['id','account_id','date','amount','description','category'])
            else:
                writer = csv.writer(csvfile)
                writer.writerow(['id','month','category','limit_amount'])
        return

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            cls_list.clear()

            def safe_float(value):
                try:
                    return float(str(value).replace(',', '.'))
                except:
                    return 0

            for row in reader:
                if cls == CashAccount:
                    cls_list.append(cls(row['id'], row['name'], row['currency']))

                elif cls == BankAccount:
                    cls_list.append(cls(row['id'], row['name'], row['currency']))

                elif cls == ExpenseTransaction:
                    amount = safe_float(row['amount'])
                    cls_list.append(cls(
                        trans_id=row['id'],
                        account_id=row['account_id'],
                        date=row['date'],
                        amount=-abs(amount),
                        description=row['description'],
                        category=row['category']
                    ))

                elif cls == IncomeTransaction:
                    amount = safe_float(row['amount'])
                    cls_list.append(cls(
                        trans_id=row['id'],
                        account_id=row['account_id'],
                        date=row['date'],
                        amount=amount,
                        description=row['description'],
                        category=row['category']
                    ))

                elif cls:
                    cls_list.append(cls(**row))
                else:
                    cls_list.append(row)

    except Exception as e:
        raise StorageError(f"Error loading CSV: {e}")
