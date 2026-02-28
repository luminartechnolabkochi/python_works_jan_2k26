

"""
string : sequence of characters 

create

variable_name = "test"

char = 'a'




"""

address = """  address line 1 address line 2"""

print(type(address)) # address is a object of class str

number = 123

print(type(number))# number is a object of class  int

is_active = True # is_active is a object of class bool

avg=4.6# avg is an object of class float


# OOPs (object oriented programming)
#using  class and object
# class plan,blueprint,template for creating objects 
# object : realworld entity

class Person:

    def eat(self):
        print("person is eating")

    def sleep(self):

        print("sleeping")

    def walk(self):

        print("walking")

# variable_name = classname()


alan_instance = Person()

alan_instance.eat()

alan_instance.sleep()

alan_instance.walk()

