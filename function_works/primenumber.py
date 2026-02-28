# w.a.p to display number is prime or not


# 
def is_prime_number(num):

    is_prime = True

    for i in range(2,num):

        if num%i==0:
            is_prime = False
            break
    print(is_prime)

is_prime_number(7)
is_prime_number(11)
is_prime_number(15)
    