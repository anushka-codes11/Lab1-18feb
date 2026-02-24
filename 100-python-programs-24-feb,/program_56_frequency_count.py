from collections import Counter
lst = list(map(int, input().split()))
freq = Counter(lst)
for k in sorted(freq.keys()):
    print(k, freq[k])

    // input : 
    1 2 2 3 1 1
    //output: 
    1 3
    2 2
    3 1
    