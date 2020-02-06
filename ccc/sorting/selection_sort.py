from time import time
from random import randint


def selection_sort(a):
    start = time()
    # take the smallest element, then exchange it with the first element.
    # take the second smallest element, then exchange it with the second element.
    # follow this pattern.
    if len(a) <= 1:
        return a
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                # low = i
                a[i], a[j] = a[j], a[i]
    return a, "ELAPSED TIME: {}".format(time() - start)


a = [randint(0, 10000) for x in range(1000)]
print(selection_sort(a))
