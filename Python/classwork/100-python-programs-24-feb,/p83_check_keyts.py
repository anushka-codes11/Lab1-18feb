n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

key = input()
print("Yes" if key in d else "No")

// input :
2
a 10
b 20
a
// output: 
  yes 