import pytest
from managers.account_manager import AccountManager
from managers.transaction_manager import TransactionManager
from managers.budget_manager import BudgetManager
from models.account import CashAccount, BankAccount
from models.transaction import ExpenseTransaction, IncomeTransaction
from models.budget import Budget
from exceptions import ValidationError, NotFoundError

# ========================
# Unit Tests
# ========================

def test_account_manager_crud():
    am = AccountManager()
    
    am.create_account("A1", "Wallet", "cash", "HUF")
    assert len(am.accounts) == 1
    assert am.accounts[0].name == "Wallet"
    
    am.update_account("A1", name="My Wallet")
    assert am.accounts[0].name == "My Wallet"
    
    am.delete_account("A1")
    assert len(am.accounts) == 0

def test_transaction_manager_crud():
    tm = TransactionManager()
    
    tm.create_transaction("T1", "A1", "2025-11-16", 100, "Grocery", "Food", "expense")
    assert tm.transactions[0].amount == -100
    
    tm.create_transaction("T2", "A1", "2025-11-16", 200, "Salary", "Income", "income")
    assert tm.transactions[1].amount == 200
    
    tm.delete_transaction("T1")
    assert len(tm.transactions) == 1

def test_budget_manager_crud():
    bm = BudgetManager()
    
    bm.create_budget("B1", "2025-11", "Food", 1000)
    assert len(bm.budgets) == 1
    
    bm.update_budget("B1", limit_amount=1200)
    assert bm.budgets[0].limit_amount == 1200
    
    bm.delete_budget("B1")
    assert len(bm.budgets) == 0

# ========================
# Integration Test
# ========================

def test_account_transaction_integration():
    am = AccountManager()
    tm = TransactionManager()
    
    am.create_account("A1", "Wallet", "cash", "HUF")
    tm.create_transaction("T1", "A1", "2025-11-16", 150, "Groceries", "Food", "expense")
    
    assert tm.transactions[0].account_id == am.accounts[0].id

# ========================
# System Test
# ========================

def test_system_workflow():
    am = AccountManager()
    tm = TransactionManager()
    bm = BudgetManager()
    
    am.create_account("A1", "Wallet", "cash", "HUF")
    
    tm.create_transaction("T1", "A1", "2025-11-16", 200, "Salary", "Income", "income")
    
    bm.create_budget("B1", "2025-11", "Food", 1000)
    
    assert len(am.accounts) == 1
    assert len(tm.transactions) == 1
    assert len(bm.budgets) == 1
