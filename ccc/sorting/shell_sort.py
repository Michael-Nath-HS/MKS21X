from random import randint


def shell_sort(a):
    n = len(a)
    h = 1
    while h < int(n / 3):
        h = (3*h) + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and a[j] < a[j - h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h = int(h/3)
    return a


a = [randint(0, 10000) for x in range(1000)]
print(shell_sort(a))
