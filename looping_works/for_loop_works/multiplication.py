

number = 2

"""
1 * 2 = 2
2 * 2 = 4
3 * 2 = 6
4 * 2 = 8
"""

for i in range(1,11):

    result = i*number

    print(f"{i} x {number} = {result}")

# 12
# 1,2,3,4,6,12

# 15
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

# 15%1==0 => 1
# 15%2==0 =>X
# 

number = 9

for i in range(1,number+1): #[1,2,3,4,5,6,7,8,9]

    if number%i==0:#9%3==0

        print(i)#1 3 9


