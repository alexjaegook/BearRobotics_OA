class Account:
    def __init__(self, account_number: str, account_type: str, pin: str, balance: int=0) -> None:
        self.account_number = account_number
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def verify_pin(self, pin: str) -> bool:
        return self.pin == pin

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        self.balance -= amount

    def get_balance(self) -> int:
        return self.balance
