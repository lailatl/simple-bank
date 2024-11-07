import unittest
from account import Account

class TestAccount(unittest.TestCase):
    # Teste da função de saque (withdraw)
    def setUp(self):
        self.account = Account(initial_balance=100)
        self.account2 = Account(initial_balance=200)
    
    def test_withdraw_success(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
    
    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)
    
    #Teste da função de depósito
    def test_deposit_success(self):
        self.account.deposit(50)                      # para amount > 0
        self.assertEqual(self.account.balance, 150)
    
    def test_deposit_negative_amount(self):          # para amount < 0
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    # Teste da função de transferencia (transfer)
    def test_transfer_success(self):
        self.account.transfer(self.account2, 50)
        self.assertEqual(self.account2.balance, 250)
        self.assertEqual(self.account.balance, 50)
    
    def test_transfer_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.account2, -30)

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.transfer(self.account2, 130)
    
if __name__ == '__main__':
    unittest.main()
