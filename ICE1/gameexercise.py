import random

pick = int(random.randint(0, 9))
#print("Chosen number:",pick)

sel = int

while pick != sel:
    sel = int(input("Enter a number:"))
    if sel < pick:
        print("Match is less")
    elif sel > pick:
        print("Match is higher")
    else:
        print("Match is perfect")