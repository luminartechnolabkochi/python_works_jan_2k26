

"""
sum of even numbers upto n

"""

limit = int(input("enter limit "))

i = 1

sum = 0

while(i<=limit):

    if i%2==0:

        sum=sum+i
    i+=1

print(sum)



