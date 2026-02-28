



# or logical 
# | bitwize or

# 2 | 4

# 0=>0000
# 1=>0001
# 2=>0010
# 3=>0011
# 4=>0100
# 5=>0101
# 6=>0110
# 7=>0111

# 0010
# 0100
# ====
# 0110

print(2|4)
print(3&2)
#0011
#0010
# ===
#0010

month = input("enter month") #JAN

match month:

    case "JAN" | "MAR" | "MAY" | "JULY" | "AUG" |"OCT"|"DEC":

        print(31)

    case "APR"|"JUNE"|"SEP"|"NOV":

        print(30)

    case "FEB":

        print(28)

    case _:

        print("invalid") 




