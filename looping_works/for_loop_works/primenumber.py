
number = int(input("enter number"))#6

is_prime = True

for i in range(2,number):

    if number%i==0:

        is_prime=False

        break

print(is_prime)


