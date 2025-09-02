"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number not in accounts:
        accounts.update({account_number: {"name": name}})
        for key, value in kwargs.items():
            accounts[account_number].update({key: value})
    else:
        return "account number already exists"
    return accounts

def deposit(account_number, amount):
    """Deposit money into account.
        return "Account not found!" (if account does not exists)
        return Deposited {amount} into {accounts name}'s account. if account exists
    """
    if account_number in accounts:
        if "account_balance" in accounts[account_number]:
            accounts[account_number].update({"account_balance": (accounts[account_number]["account_balance"] + amount)}) 
        else:
            accounts[account_number].update({"account_balance": amount})
        return f"Deposited {amount} into {accounts[account_number]['name']}'s account \nBalance: {accounts[account_number]['account_balance']}"
        
    else:
        return "Account not found"

def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds"""
    if account_number in accounts:
        if "account_balance" in accounts[account_number]:
            if accounts[account_number]["account_balance"] >= amount:
                accounts[account_number].update({"account_balance": accounts[account_number]["account_balance"] - amount})
                return f"{amount} has been deducted from {accounts[account_number]['name']}'s account \nBalance: {accounts[account_number]['account_balance']}"
            else:
                return "Insufficient funds!"
        else:
            return "Insufficient funds!"
    else:
        return "Account not found"

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts. if funds is sufficient"""

    if from_acc in accounts:
        if to_acc in accounts:
            if "account_balance" in accounts[from_acc]:
                if accounts[from_acc]["account_balance"] >= amount:
                    accounts[from_acc].update({"account_balance": accounts[from_acc]["account_balance"] - amount})
                else:
                    return "Insufficient funds"

                if "account_balance" in accounts[to_acc]:
                    accounts[to_acc].update({"account_balance": accounts[to_acc]["account_balance"] + amount})
                else:
                    accounts[to_acc].update({"account_balance": amount})

                return f"{amount} has been transferred from {accounts[from_acc]['name']} to {accounts[to_acc]['name']} \nSender Balance: {accounts[from_acc]['account_balance']} \nReceiver Balance: {accounts[to_acc]['account_balance']}"
                

                    
            else:
                return "Insufficient fundss"
        else:
            return "Receiver account not found"
    else:
        return "Sender account not found"

