s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
union = s1 | s2
print(*sorted(union)) 

// input : 
1 2 3
3 4 5
// output 
 1 2 3 4 5