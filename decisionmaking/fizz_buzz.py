"""
read num 15
display FIZZ if num / by 3
display BUZZ if num / by 5
display FIZZBUZZ if num / 15
else: invalid 

1)day

2)/ by 8

3)/ by 2 and 5

4) chk number in range of  50 to 100

5)odd even

6)largest of three

7)fizz buzz

DECISION MAKING []
"""

number = int(input("enter number"))#15

if number%15==0:#15%3==0

    print("FIZZBUZZ")

elif number%5==0:#25%5==0

    print("Buzz")

elif number%3==0:

    print("FIZZ")

else:

    print("invalid")