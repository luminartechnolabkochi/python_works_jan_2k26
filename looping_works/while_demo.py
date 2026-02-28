

"""
initialization
while(condition):
    stmt
    incr|decr
"""

# display all leap year from 1800 - 2026

i = 1800

while(i<=2026):

    if (i%100==0 and i%400==0) or (i%100!=0 and i%4==0):

        print(i)

    i=i+1




