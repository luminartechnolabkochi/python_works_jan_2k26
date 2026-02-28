

lst =[10,11,12,17,13,15]
#      0  1  2  3  4  5

max= 0

second_max = 0

for num in lst:  #num= 10

    if num > max:

        second_max = max#12

        max = num#17

    elif max>num and num>second_max:

        second_max = num

print(second_max)

        
