

food_logs = [

        [1,"adithya","dosa","meals","chapthy",1800],#0
        [2,"shreya","idly","biriyani","chapthy",2100],#1
        [3,"amritha","appam","meals","puttu",1700],
        [4,"dijo","protien shake","mandhi","salad",1900]
]


max_cal=max([lst[-1] for lst in food_logs ]) #2100

max_cal = [lst[1] for lst in food_logs if lst[-1]==max_cal]

print(max_cal)



# for lst in food_logs:

#     if lst[3] == "meals":

#         print(lst[1])

meals_filter = [lst[1] for lst in food_logs if lst[3]=="meals"]

print(meals_filter)

# all_names = [lst[1] for lst in food_logs ]

# print(all_names)

# all_break_fast=[lst[2] for lst in food_logs]

# print(all_break_fast)

# display names who is taking breakfast as dosa