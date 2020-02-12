
import itertools
def biggerIsGreater(w):
    w = list(w)
    start = -1;
    
    for i in range(len(w) - 1):
        if w[i] < w[i + 1]:
            start = i
    if start == -1:
        return "no answer"
    end = -1
    for j in range(len(w)):
        if w[j] > w[start]:
            end = j
    w[start], w[end] = w[end], w[start]
    a = w[start + 1:]
    a.sort()
    for i in range(start + 1, len(w)):
        w[i] = a[i - start - 1]
    print("".join(w))
biggerIsGreater("abcd")