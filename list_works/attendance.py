   # sunday->monday => attendance store
    # H => holiday
    # P=>present
    # O=>online


work_log =["H","P","P","P","P","P","L","H"]
#           0   1  2   3    4.  5   6   7



holiday_count = 0

present_count = 0

for att in work_log:

    if att == "H":

        holiday_count+=1

    elif att=="P":

        present_count+=1

print("holiday count",holiday_count)
print("present count",present_count)

# jan-dece
# [15000,16000]