class BankAccount:
    def __init__(self, input_holder_name, input_balance,
    input_account_type):
        self.holder_name = input_holder_name
        self.balance = input_balance
        self.account_type = input_account_type
        self.rates = {
            "personal": 10,
            "business": 50,
            "savings": -5
        }

    def pay_in(self, amount):
        self.balance += amount

    def pay_monthly_fee(self):
        self.balance -= self.rates[self.account_type]