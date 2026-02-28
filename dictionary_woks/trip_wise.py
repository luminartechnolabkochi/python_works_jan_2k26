

manali={

    "dijo":300,# 2514-300
    "akshay":1000,#2514-1000
    "edwin":800,
    "alan":15000,
    "manoj":0,
    "subin":0,
    "sreyesh":500,
    
}

total_expens=0

for v in manali.values():

    total_expens+=v

print("total Exp",total_expens)

individual_split = round(total_expens/len(manali))

print(individual_split)

spend_wise={}

for k,v in manali.items():

    payment = individual_split - v

    spend_wise[k] = payment

print(spend_wise)

