class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def verify_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
