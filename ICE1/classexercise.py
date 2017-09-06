# Class Exercise #2

import math
print("Give the radius")

rad = float(input("enter the radius: "))

circ = 2*math.pi*rad
print("Circumference is: ", circ)

area = math.pi*rad*rad
print("Area is: ", area)

check = rad%2

if check==0:
    print("Radius is even")
else:
    print("Radius is odd")