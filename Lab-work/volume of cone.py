import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

l = math.sqrt(r*r + h*h)
csa = math.pi*r*l
tsa = math.pi*r*(l+r)
vol = (1/3)*math.pi*r*r*h

print("Curved Surface Area =", csa)
print("Total Surface Area =", tsa)
print("Volume =", vol)