import unittest
from BankSystem import BankSystem

class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.bank = BankSystem()

    def test_verify_pin(self):
        self.assertTrue(self.bank.verify_pin("1234567", "1234"))
        self.assertFalse(self.bank.verify_pin("1234567", "4321"))
        self.assertFalse(self.bank.verify_pin("9999999", "1234"))

    def test_get_accounts(self):
        accounts = self.bank.get_accounts("1234567").get("accounts")
        self.assertIn("checking", accounts)
        self.assertIn("savings", accounts)
        self.assertEqual(accounts["checking"].get_balance(), 1000)
        self.assertEqual(accounts["savings"].get_balance(), 1500)

if __name__ == "__main__":
    unittest.main()
