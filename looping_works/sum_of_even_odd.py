

"""
w.a.p display sum of odd_numbers and sum_of_even_numbers upto limit 6

"""


limit = int(input("enter limit"))


i = 1 

even_sum=0

odd_sum=0

while(i<=limit):

    if i%2==0:

        even_sum = even_sum+i
    else:
        odd_sum = odd_sum+i

    i+=1

print("odd sum",odd_sum)

print("even sum",even_sum)
