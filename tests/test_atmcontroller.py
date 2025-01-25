import unittest
from BankSystem import BankSystem
from ATMController import ATMController

class TestATMController(unittest.TestCase):
    def setUp(self):
        self.bank = BankSystem()
        self.atm = ATMController(self.bank)

    def test_atm_workflow(self):
        # Insert Card
        self.atm.insert_card("1234567")

        # Enter PIN
        self.atm.enter_pin("1234")

        # Select Account
        self.atm.select_account("checking")

        # Check Balance
        self.assertEqual(self.atm.check_balance(), 1000)

        # Deposit
        self.atm.deposit(500)
        self.assertEqual(self.atm.check_balance(), 1500)

        # Withdraw
        self.atm.withdraw(200)
        self.assertEqual(self.atm.check_balance(), 1300)

        # Eject Card
        self.atm.eject_card()
        self.assertIsNone(self.atm.current_card)
        self.assertIsNone(self.atm.current_accounts)
        self.assertIsNone(self.atm.selected_account)

    def test_invalid_card(self):
        with self.assertRaises(ValueError):
            self.atm.insert_card("9999999")

    def test_incorrect_pin(self):
        self.atm.insert_card("1234567")
        with self.assertRaises(ValueError):
            self.atm.enter_pin("4321")

    def test_invalid_account_selection(self):
        self.atm.insert_card("1234567")
        self.atm.enter_pin("1234")
        with self.assertRaises(ValueError):
            self.atm.select_account("nonexistent")

if __name__ == "__main__":
    unittest.main()
