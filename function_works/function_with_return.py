
# function with parameter and return value

# return 

# def function_name(p1,p2):

#     return value


def addition(n1,n2):

    result = n1+n2#300

    return result#return 300


# print(addition(100,200))

# create a function smart_sub with two parameter n1,n2
# return subtarction result as n1-n2 if n1>n2 else return n2-n1

# sub(20,8)12
# sub(8,20)12

def smart_sub(n1,n2):

    if n1>n2:

        return n1-n2
    
    else:

        return n2-n1
    
print(smart_sub(10,20))
print(smart_sub(20,10))
# create a function is_odd with param num return True if num is odd else return False
# create a function is_even with param num return True if num is even else return False
# create a function is_positive with param num return True if num is positive else return False
# create a function is_zero with param num return True if num is zero else return False



def is_even(num):

    is_even_number = num%2==0

    return is_even_number



def is_zero(num):

    if num==0:

        return True
    else:

        return False
    



def exponent(base,pow=2):

    result=base**pow

    return result


print(exponent(10,pow=3))


# create a function calculator with n1,n2,op
# if op==+ return addition  of n1 ,n2
# if op==- return sub of n1 ,n2
# if op==* return mul of n1 ,n2
# if op==/ return div of n1 ,n2


# calculator(10,5,op="*")
# calculator(10,5,op="-")
# calculator(10,5,op="/")
# calculator(10,5) # default addition

# String
