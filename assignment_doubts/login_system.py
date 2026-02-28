"""
✅ 3. Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"

"""

db_password = "Password@123"

db_otp = "2121"


user_password = input("enter password")


if db_password == user_password:

    user_otp = input("enter otp")

    if db_otp == user_otp:

        print("login success")
    else:

        print("incorrect otp")

else:

    print("incorrect [password]")




