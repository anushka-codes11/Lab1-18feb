n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
for k in sorted(d):
    print(k, d[k])

    /// input : 
    3
   c 30
   a 10
   b 20
   // output : 
     a 10
     b 20
     c 30
