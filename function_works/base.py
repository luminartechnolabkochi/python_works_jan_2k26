

# create a function max_two with two parameter num1,num2
# display largest number

def max_two(num1,num2):

    if num1>num2:

        print(num1)
    else:
        print(num2)

max_two(100,200)

# create a function last_digit_max with two parameter num1,num2
# display num1 if last_digit of num1 > last digit of num2
# display num2 if last_digit of num2 > last digit of num2

# last_digit_max(127,892) # 127
# last_digit_max(127,98) # 98

def last_digit_max(num1,num2):

    n1_ld = num1%10

    n2_ld = num2%10

    if n1_ld>n2_ld:
        print(num1)
    elif n2_ld>n1_ld:
        print(num2)
    else:
        print(num1,num2)

last_digit_max(187,892)
last_digit_max(187,87)

