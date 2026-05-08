lst = list(map(int, input().split()))
unique_lst = list(set(lst))
unique_lst.sort()
print(unique_lst[-2] if len(unique_lst) > 1 else unique_lst[0])


// input :
  4 5 1 5 3
// outpyut :  
     4