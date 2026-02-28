"""
ask:
- Ask for unlock pattern

If pattern is correct:
    - Ask for fingerprint
    - If fingerprint matches:
        "Phone unlocked"
    - Else:
        "Fingerprint mismatch"
Else:
    "Wrong pattern"

"""

db_pattern="v"

db_finger_print="zzzzzvvvv"


user_pattern=input("enter pattern")

if db_pattern == user_pattern:

    user_finger_print = input("enter finger print")

    if db_finger_print == user_finger_print:

            print("Phone unlocked") 
    else:
          print("invalid finger print")

else:

      print("pattern incorrect")       