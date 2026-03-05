"""
Error handling
   

try:
    doubtfull code

except:

    handling code
"""

lst=[10,11,12,13,14]
#     0  1  2  3  4

index = int(input("enter index pos"))

try:
    print(lst[index])

except Exception as e:

    print(e)

print("dabase commit")
print("file write")

