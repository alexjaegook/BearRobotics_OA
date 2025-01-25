from BankSystem import BankSystem

class ATMController:
    def __init__(self, bank_system):
        self.bank_system = bank_system
        self.current_card = None
        self.current_accounts = None
        self.selected_account = None

    def insert_card(self, card_number: str) -> None:
        if card_number not in self.bank_system.accounts:
            raise ValueError("Invalid card.")
        self.current_card = card_number
        print(f"Card {card_number} inserted.")

    def enter_pin(self, pin: str) -> None:
        if not self.current_card:
            raise ValueError("No card inserted.")
        if not self.bank_system.verify_pin(self.current_card, pin):
            raise ValueError("Incorrect PIN.")
        self.current_accounts = self.bank_system.get_accounts(self.current_card).get("accounts")
        print("PIN verified.")

    def select_account(self, account_type: str) -> None:
        if not self.current_accounts or account_type not in self.current_accounts:
            raise ValueError("Invalid account selection.")
        self.selected_account = self.current_accounts[account_type]
        print(f"Account {account_type} selected.")

    def check_balance(self) -> int:
        if not self.selected_account:
            raise ValueError("No account selected.")
        return self.selected_account.get_balance()

    def deposit(self, amount: int) -> None:
        if not self.selected_account:
            raise ValueError("No account selected.")
        self.selected_account.deposit(amount)
        print(f"Deposited ${amount}.")

    def withdraw(self, amount: int) -> None:
        if not self.selected_account:
            raise ValueError("No account selected.")
        self.selected_account.withdraw(amount)
        print(f"Withdrew ${amount}.")

    def eject_card(self) -> None:
        print(f"Card {self.current_card} ejected.")
        self.current_card = None
        self.current_accounts = None
        self.selected_account = None
