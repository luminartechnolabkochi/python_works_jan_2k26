


expenses = [22000,27000,29000,32000,31000,25000,23000]
#             0     1    2    3     4      5      6
#             j     f    m       


total_expense = 0


for e in expenses:

    total_expense+=e


print("total expense",total_expense)

print("avg expense",total_expense/len(expenses))

print(dir(list))