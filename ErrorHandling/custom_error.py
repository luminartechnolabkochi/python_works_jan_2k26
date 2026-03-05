

# Error => zero division error
#          indexerror
#          FileNotFOund
#         KeyError


age = int(input("enter age"))

if age<18:

    raise Exception("invalid age")

else:

    print("access granted")
