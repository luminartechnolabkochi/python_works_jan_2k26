stock_list1=[10,11,12,13,14,15]

stock_list2=[20,21,22,23,24,25]

combined_list=[]

combined_list.extend(stock_list1)

combined_list.extend(stock_list2)

print(combined_list)

updated_list =[]

for num in combined_list:

    updated_list.append(num+5)

print(updated_list)

