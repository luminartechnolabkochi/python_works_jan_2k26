

number = 123

total = 0

while(number!=0):#123!=0 12!=0 1!=0

    last_digit = number%10#ld=123%10=>3 2 1

    total = total + last_digit # total = 0+3=3+2=>5+1=>6

    number =  number//10# 12//10=1 =0

print(total)
