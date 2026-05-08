s = input()
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
for k in sorted(freq):
    print(k, freq[k])

    // input : 
     banana
     //output : 
     a 3
     b 1
     n 2