n=5
for i in range(n):
    for j in range(n):
        if i==2 or j==2:
            print("*",end="")
        else:
            print(" ",end="")
    print()