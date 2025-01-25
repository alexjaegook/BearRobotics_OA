from Account import Account

class BankSystem:
    def __init__(self) -> None:
        # Have a card number associated with the Account
        # Key: Card Number
        # Value: The Accounts associated with the card
        self.accounts = {
            "1234567": {
                "pin": "1234",
                "accounts": {
                    "checking": Account("0000", "checking", 1000),
                    "savings": Account("0001", "savings", 1500),
                },
            }
        }

    def verify_pin(self, card_number: str, pin: str) -> bool:
        return self.accounts.get(card_number, {}).get("pin") == pin

    def get_accounts(self, card_number: str):
        return self.accounts.get(card_number, {})
