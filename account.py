class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self.balance += amount

    def transfer(self, account2, amount):
        if amount < 0: 
            raise ValueError("Cannot transfer negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        account2.balance += amount
 