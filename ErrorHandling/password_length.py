

password = input("enter password")

if len(password) < 6:

    raise Exception("password invalid")

else:
    print("ok.")