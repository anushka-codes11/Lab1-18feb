lst = list(map(int, input().split()))
print(*list(dict.fromkeys(lst))) 

// input : 
  1 2 2 3 1 4
// output : 
   1 2 3 4