from modules.bank_account import *
import pdb

# account = {
#     "holder_name": "Colin",
#     "balance": 100,
#     "type": "business"
# }

bank_account = BankAccount("Colin", 100, "business")
bank_account2 = BankAccount("John", 1000000, "personal") 
bank_account3 = BankAccount("Hannah", 40, "savings")
# pdb.set_trace()

print (bank_account.balance)
print (bank_account2.balance)
print (bank_account3.balance)

bank_account.pay_monthly_fee()
bank_account2.pay_monthly_fee()
bank_account3.pay_monthly_fee()

print (bank_account.balance)
print (bank_account2.balance)
print (bank_account3.balance)





