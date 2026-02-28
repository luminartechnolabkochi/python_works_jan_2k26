# read three mark m1,m2,m3 each out of 50
# find total
# display A if total >140
# display B if total in range of 130 - 140
# display C if total in range of 120 - 130
# display Fail anything below 120 

mark1 = int(input("enter mark1"))#30
mark2 = int(input("enter mark2"))#30
mark3 = int(input("enter mark3"))#30

total = mark1+mark2+mark3#90

if total>140:#90>140

    print("A")

elif total>130:#90>130

    print("B")

elif total>120:#90>120

    print("C")
else:

    print("failed")

