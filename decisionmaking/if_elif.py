"""
if condition1:
    stmt1

elif condition2:
    stmt2

elif condition3:
    stmt3

else:
   default

"""

num1 = int(input("enter num1"))#10

num2 = int(input("enter num2"))#20

num3 = int(input("enter num3"))#30


if num1>num2 and num1>num3:# 10>20 [False] and 10>30 

    print("num1 is largest",num1)

elif num2>num1 and num2>num3:# 20>10 [T] and 20 > 30[F]

    print("num2 is largest",num2)

elif num3>num1 and num3>num2:# 30>10 [T] and 30>20[T]

    print("num3 is largest",num3)