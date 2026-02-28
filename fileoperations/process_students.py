

fr_all_students=open("fileoperations\\all_students.txt","r")

fr_passed_students = open("fileoperations\\passed_students.txt","r")

all_students_list=[line.rstrip("\n") for line in fr_all_students]

passed_students_list = [line.rstrip("\n") for line in fr_passed_students]

print("all",all_students_list)

print("pass",passed_students_list)

failed_students = set(all_students_list).difference(passed_students_list)

print("failed",failed_students)