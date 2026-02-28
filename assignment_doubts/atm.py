"""
✅ 5. ATM Withdrawal

Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"

"""


db_pin = 123123

db_balance = 50000


user_pin =int(input("enter pin : "))

if db_pin == user_pin:

    amount = int(input("enter transaction amount"))

    if amount<=db_balance:

        print("Withdrawal successful")
    else:

        print("insufficient balance")
else:

    print("incorrect pin")