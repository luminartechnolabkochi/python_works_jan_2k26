

"""
initialization
while(condition):
    stmts
    incr/decr

"""






# w.a.p display divisors of 16

number = int(input("enter number "))

number_copy = number 

result = 0

while(number!=0):

    digit = number % 10

    result = result*10+digit

    number = number//10

if result==number_copy:

    print("palindrome")

else:
    print("not plaindrome")

