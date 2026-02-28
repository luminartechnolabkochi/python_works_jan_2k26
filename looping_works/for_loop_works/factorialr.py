num=4
# 1*2*3*4

fact = 1
for i in range(1,num+1): # i=4(1,2,3,4)

    fact = fact*i #fact = fact=6*4=24


print(fact)#24


num = 15

# 1+2+3+4+5+6+7+8+9+10

fact = 0
for i in range(1,num+1):

    fact = fact + i

print(fact)

number = 10

# 1,2,3,4,5,6,7,8,9,10
# i

for i in range(1,number+1):

    if number%i==0:

        print(i)


# w.a.p to display numbers that are divisible by 3  from 1 => 25

for i in range(1,26):

    if i%3==0:

        print(i)