from BankSystem import BankSystem
from ATMController import ATMController

# Testing the ATM Controller
if __name__ == "__main__":
    # Initialize a bank system
    bank_system = BankSystem()

    # Initializing ATM controller
    atm = ATMController(bank_system)

    # NOTE: If you want to add more bank accounts, add them to the BankSystem
    try:
        # Simulate the workflow
        atm.insert_card("1234567")
        atm.enter_pin("1234")       # using the correct pin
        atm.select_account("checking")
        print(f"Balance: ${atm.check_balance()}")
        atm.deposit(500)
        print(f"Balance after deposit: ${atm.check_balance()}")
        atm.withdraw(200)
        print(f"Balance after withdrawal: ${atm.check_balance()}")
        atm.eject_card()
    except ValueError as e:
        print(f"Error: {e}")
