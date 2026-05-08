n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)
    //input : 
    3
    c 30
    a 10
     b 20