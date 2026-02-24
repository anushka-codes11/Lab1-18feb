s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
sym_diff = s1 ^ s2
print(*sorted(sym_diff))

// input : 
1 2 3
3 4 5
// output : 
 1 2 3 4