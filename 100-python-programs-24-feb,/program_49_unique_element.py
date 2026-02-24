def unique_elements(lst):
    return list(set(lst))

lst = list(map(int, input().split()))
print(*unique_elements(lst))

// input: 
   1 2 2 3 4 4 5
// output: 
    1 2 3 4 5