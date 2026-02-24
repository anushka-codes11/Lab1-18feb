n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

key = input()
d.pop(key, None)

for k in sorted(d):
    print(k, d[k]) 


    // input : 
     2
a 1
b 2
a
// output : 
 b 2