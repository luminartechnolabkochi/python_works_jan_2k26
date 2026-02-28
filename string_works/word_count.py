

# w.a.p to diplay alphabet_count, digit_count,special_character_count

word="aman##aplan**panamawith2car1bike"

al_count = 0

d_count=0

sp_count = 0

for ch in word:

    if ch.isalpha():

        al_count+=1

    elif ch.isdigit():

        d_count+=1

    elif not ch.isalnum():

        sp_count+=1

print(f"alphabet count {al_count}")
print(f"digit count {d_count}")
print(f"special count {sp_count}")