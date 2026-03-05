


lst =[10,20,30,40,50,60]

index = int(input("enter index"))

try:
    
    print(lst[index])

except Exception as e:
    
    index = int(input("enter index"))    
    
    print(lst[index])

finally:

    print("file operation....")

    print("db.., commit")

# raise
# assert