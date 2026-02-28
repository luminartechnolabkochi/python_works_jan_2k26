

"""
if condition1:
    stmt1
elif condition2:
    stmt2

elif condition3:
    stmt3

"""
signal = input("enter signal")

if signal=="red":

    print("STOP")

elif signal == "green":

    print("GO")

elif signal=="yellow":

    print("wait")


num1=int(input("enter number"))
num2=int(input("enter number"))
num3=int(input("enter number"))


if num1>num2 and num1>num3:

    print(num1,"is largest")

elif num2>num1 and num2>num3:

    print(num2,"is largset")
else:
    print(num3,"is largest")
