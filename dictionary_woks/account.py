"""
Create a dictionary:
account_number
holder_name
balance
Tasks:
Deposit 5000
Withdraw 2000
Check if balance is less than 1000 → print "Low Balance"


"""

account ={"account_number":1234,"holder_name":"vipin","balance":5000}


account["balance"]+=5000

if account["balance"] > 2000:

    account["balance"]-=2000

else:

    print("insufficient balance")


if account["balance"] < 1000:

    print("low balanace")
