
number = 123

result = 0

while(number!=0):#123!=0 12!=0,2 1!=0

    digit = number% 10#3 1%10=1

    result = result*10+digit#32*10+1=321

    number = number//10#0


while(result!=0):

    digit = result% 10

    print(digit)

    number = number//10


