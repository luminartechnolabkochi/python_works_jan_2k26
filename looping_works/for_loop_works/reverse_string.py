# index 
# always starts at 0
# value sequence[index]


word=input("enter text ") 
#java
#0123
word_length = len(word)-1#3

result = ""
for i in range(word_length,-1,-1):

    result=result+word[i]

print(result)






