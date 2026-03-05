


fr = open("fileoperations\\employee.txt")

employees= []

for line in fr:
    #line ="1000,vipin,hr,25000\n"

    data=line.rstrip("\n").split(",")#[1000,"vipin","hr",25000]

    emp={"id":data[0],"name":data[1],"dept":data[2],"salary":data[3]}

    employees.append(emp)

all_names = [e.get("name") for e in employees]

print(all_names)

max_sal = max(employees,key=lambda e: e.get("salary"))
print(max_sal)





