import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

csa = 2*math.pi*r*h
tsa = 2*math.pi*r*(r+h)
vol = math.pi*r*r*h

print("Curved Surface Area =", csa)
print("Total Surface Area =", tsa)
print("Volume =", vol)