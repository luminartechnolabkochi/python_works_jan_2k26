

from csv import DictReader

fr = open("fileoperations\\tips.csv")

# csv => list_of_diction [csv.py > DictReader]

data = list(DictReader(fr))

print(data[0])#{'total_bill': '16.99', 'tip': '1.01', 'sex': 'Female', 'smoker': 'No', 'day': 'Sun', 'time': 'Dinner', 'size': '2'}

day_wise_summary ={}

for d in data:

    tip = float(d.get("tip"))

    day = d.get("day")

    if day in day_wise_summary:

        day_wise_summary[day]+=tip

    else:

        day_wise_summary[day]=tip

print(day_wise_summary)

# day_with_highest_revenue


day_wise_total={}

for d in data:

    day = d.get("day")

    total_bill = float(d.get("total_bill"))

    if day in day_wise_total:

        day_wise_total[day]+=total_bill

    else:

        day_wise_total[day]=total_bill

print(day_wise_total)


print(max(day_wise_total,key=day_wise_total.get))
# {male:123,female:456}



# list,dictionary
# set
# tuple
# oops(object oriented programming)

# csv.py > DictReader 
# csv.py > DictWriter


# ErrorHandling

# logical Error
# Syntax Error
# Runtime Error


from csv import DictReader

fr = open("fileoperations\\flight.txt") #run time error X

data = list(DictReader(fr))

print("line1")
print("line1")
print("line1")
print("line1")
print("line1")
