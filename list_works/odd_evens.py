

numbers =[10,11,12,13,14,15,17,3,2,1,3,4]

# w.a.p to create two new list from numbers ie odd_list and even_list

even_list = []

odd_list= []

for num in numbers:

    if num%2==0:

        even_list.append(num)
    else:
        odd_list.append(num)

print("even",even_list)
print("odd",odd_list)




