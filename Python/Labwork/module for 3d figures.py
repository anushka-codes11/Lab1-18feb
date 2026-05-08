import math

# Cube
def cube(side):
    tsa = 6*side*side
    vol = side**3
    return tsa, vol

# Cuboid
def cuboid(l,b,h):
    tsa = 2*(l*b + b*h + l*h)
    vol = l*b*h
    return tsa, vol

# Cylinder
def cylinder(r,h):
    csa = 2*math.pi*r*h
    tsa = 2*math.pi*r*(r+h)
    vol = math.pi*r*r*h
    return csa, tsa, vol

# Cone
def cone(r,h):
    l = math.sqrt(r*r + h*h)
    csa = math.pi*r*l
    tsa = math.pi*r*(l+r)
    vol = (1/3)*math.pi*r*r*h
    return csa, tsa, vol

# Sphere
def sphere(r):
    tsa = 4*math.pi*r*r
    vol = (4/3)*math.pi*r**3
    return tsa, vol

# Hemisphere
def hemisphere(r):
    csa = 2*math.pi*r*r
    tsa = 3*math.pi*r*r
    vol = (2/3)*math.pi*r**3
    return csa, tsa, vol