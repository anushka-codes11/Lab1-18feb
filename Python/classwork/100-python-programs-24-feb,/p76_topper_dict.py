n = int(input())
marks = {}
for _ in range(n):
    name, mark = input().split()
    marks[name] = int(mark)
topper = max(marks, key=marks.get)
print(topper)

// input : 
3
Alice 85
Bob 90
Charlie 88

// output : 
Bob