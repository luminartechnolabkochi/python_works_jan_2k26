"""
Create a dictionary to store a student's details:
id
name
course
marks
Tasks:
    a)Print the student name
    b)Update marks by adding 5 bonus marks
    c)Add a new key grade
    d)Check if attendance key exists

"""



student={"id":1,"name":"vipin","course":"django","marks":123}
#          0           1               2              3

print(student["name"])

student["marks"]+=5

student["grade"]="A+"

if "attendance" in student:

    print("yes")

else:
    print("no")

print(student)
