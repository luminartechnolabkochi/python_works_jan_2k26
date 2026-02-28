

number = int(input("enter number"))#123

number_copy=number

result = 0

number_length = len(str(number))

while(number!=0):

    digit = number%10

    expo = digit**number_length

    result = result+expo

    number = number//10

if number_copy == result:

    print("armstrong")

else:

    print("not armstrong")