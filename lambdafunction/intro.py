

"""
lambda function

defnition : anonymous function with single expression

syntax:

var_name = lambda p1,p2:experssion

"""


add_number =  lambda n1,n2 : n1+n2

print(add_number(100,200))

sub_number = lambda n1,n2:n1-n2

print(sub_number(100,20))

cube = lambda n : n**3

print(cube(3))


odd_even= lambda num : "even" if num%2==0 else "odd"

print(odd_even(10))

# create a lambda function is_positive return True if number is positive else return False

is_positive = lambda num : num > 0



