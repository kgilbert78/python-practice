from datetime import date

class BankAccount:
    def __init__(self, date_opened, initial_amt=0.0):
        self.date_opened = date_opened # format: date(2021, 3, 15)
        self._balance = initial_amt
        self._deposits = []
        self._withdrawals = []

    def make_deposit(self, amt):
        self._balance += amt
        self._deposits.append(amt)

    def make_withdrawal(self, amt):
        self._balance -= amt
        self._withdrawals.append(amt)

    def get_balance(self):
        return self._balance
    def get_deposits(self):
        deposits_copy = self._deposits[:]
        return deposits_copy
    def get_withdrawals(self):
        withdrawals_copy = self._withdrawals[:]
        return withdrawals_copy

# make child classes for checking accounts & savings accounts to practice inheritance. 

class SavingsAccount(BankAccount):
    def __init__(self, date_opened, initial_amt, interest_rate):
        super().__init__(date_opened, initial_amt=initial_amt)
        self.interest_rate = interest_rate
        # to calculate compound interest annually I'll need to add dates on all deposits and withdrawals to know the principal at each anniversary.
        

# date opened format: date(2021, 3, 15)
my_acct = SavingsAccount(date(2020, 3, 15), 0, .01)
print(my_acct.interest_rate)
my_acct.make_deposit(500)
my_acct.make_deposit(200)
print(my_acct._balance, my_acct._deposits)
my_acct.make_withdrawal(100)
print(my_acct._balance, my_acct._withdrawals)
    