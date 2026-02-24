n = int(input())
d1 = {}
for _ in range(n):
    k, v = input().split()
    d1[k] = int(v)
m = int(input())
d2 = {}
for _ in range(m):
    k, v = input().split()
    d2[k] = int(v)
merged = {**d1, **d2}
for k in sorted(merged):
    print(k, merged[k])

    // input : 
 2
a 1
b 2
2
b 3
c 4
// output : 
 a 1
b 3
c 4