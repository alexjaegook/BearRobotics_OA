import unittest
from Account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("0000", "checking", 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 800)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-200)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

if __name__ == "__main__":
    unittest.main()
