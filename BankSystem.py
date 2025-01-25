import Account

class BankSystem:
    def __init__(self) -> None:
        # Have a card number associated with the Account
        # Key: Card Number
        # Value: The Accounts associated with the card
        self.accounts = {
            "1234567": {
                "checking" : Account("4567", "checking", "1234", 1000),
                "saving" : Account("09987", "saving", "1234", 1500)
            }
        }

    def verify_pin(self, card_number: str, pin: str) -> bool:
        account = self.accounts.get(card_number, {})

        return any(account.verify_pin(pin) for account in accout.values())

    def get_accounts(self, card_number: str) -> dict(str, dict(str, Account)):
        return self.accounts.get(card_number, {})
