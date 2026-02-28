numbers=[-1,-1,10,11,12,13,-13,-15,4,5]
# w.a.p create two list postive_list,negative_list

p_list = []

n_list=[]

for num in numbers:

    if num>0:
        p_list.append(num)

    elif num<0:

        n_list.append(num)

print("posit",p_list)
print("neg",n_list)

