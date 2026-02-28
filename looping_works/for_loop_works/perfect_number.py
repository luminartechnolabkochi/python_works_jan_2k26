# perfectnumber

# number = 6
# 1,2,3,4,5
# 1+ 2+3=6

# 14
# 1,2,3,4,5,6,7,8,9,10,11,12,13
# 1+2+7=10

# 28
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,,,,,,,27
# 1+2+4+7+14=28

number = int(input("enter number"))

sum = 0

for i in range(1,number):

    if number%i==0:

        sum = sum+i

if number==sum:
    print("perfect number")
else:
    print("not perfect number")