lst = list(map(int, input().split()))
evens = [x for x in lst if x % 2 == 0]
odds = [x for x in lst if x % 2 != 0]
print("Even:", *evens)
print("Odd:", *odds)

//input : 
 1 2 3 4 5 6 
//output: 
Even: 2 4 6
Odd: 1 3 5