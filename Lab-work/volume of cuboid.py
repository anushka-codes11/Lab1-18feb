l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

csa = 2*h*(l+b)
tsa = 2*(l*b + b*h + l*h)
vol = l*b*h

print("Curved Surface Area =", csa)
print("Total Surface Area =", tsa)
print("Volume =", vol)