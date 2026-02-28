def is_fibonacci_number(number): #9
    is_fibo = False
    prev = 0
    curr = 1
    next = prev + curr#1
    while(next<=number):

        next = prev + curr

        prev = curr

        curr = next

        if next==number:

            is_fibo = True

            break

    return is_fibo
print(is_fibonacci_number(3))
print(is_fibonacci_number(5))
print(is_fibonacci_number(8))
print(is_fibonacci_number(10))