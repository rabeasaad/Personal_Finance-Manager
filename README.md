# Personal Finance Manager

A simple **command-line Personal Finance Manager** written in Python.  
This application allows you to **manage accounts, transactions, and budgets**, and save/load your data using CSV files.

---
Project Structure
personal_finance/
├── main.py
├── models/
│   ├── account.py
│   ├── transaction.py
│   └── budget.py
├── managers/
│   ├── account_manager.py
│   ├── transaction_manager.py
│   └── budget_manager.py
├── storage/
│   └── csv_storage.py
├── tests/
│   └── test_finance.py
├── README.md
└── requirements.txt

## Features

- **Accounts**
  - List all accounts
  - Create new accounts (Cash or Bank)
  - Update existing accounts
  - Delete accounts

- **Transactions**
  - List all transactions
  - Create expense or income transactions
  - Update transactions
  - Delete transactions

- **Budgets**
  - List budgets
  - Create budgets with monthly limits
  - Update budgets
  - Delete budgets

- **CSV Storage**
  - Save all data to CSV files
  - Load data from CSV files

---

## Requirements

- Python 3.10 or higher
- Packages listed in `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt

Activate your virtual environment (optional but recommended):
# Windows PowerShell
venv\Scripts\Activate.ps1

# or Windows CMD
venv\Scripts\activate

Run the main program:
python main.py
Use the menu options to manage accounts, transactions, and budgets
Save or load data using the CSV options in the main menu
You will see the main menu:
1. Manage Accounts
2. Manage Transactions
3. Manage Budgets
4. Save to CSV
5. Load from CSV
6. Exit

Make sure pytest is installed:
pip install pytest

Run automated tests using pytest:
pytest

Run tests with verbosity (-v)
Shows detailed information about each test, including test names:
pytest -v

Run tests quietly (-q)
Only shows summary results:
pytest -q

Run tests by marker (-m <marker>)
If you use markers to categorize tests (e.g., @pytest.mark.budget), you can run only those tests:
pytest -m budget

python -m pytest -v


























