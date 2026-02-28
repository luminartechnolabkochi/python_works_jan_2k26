"""
Task:
- Ask for age

If age ≥ 18:
    - Ask for seat availability
    - If seats available:
        "Ticket booked"
    - Else:
        "House full"
Else:
    "Not eligible to watch the movie"

"""

avail_seats = 14

age = int(input("enter age"))

if age>=18:

    seat_count = int(input("enter no of seat"))

    if avail_seats<=seat_count:

        print("tickets booked")
    else:

        print("not available")

else:
    print("invalid age")


# if..else

"""
if  

elif 

else

match

case

looping
"""
