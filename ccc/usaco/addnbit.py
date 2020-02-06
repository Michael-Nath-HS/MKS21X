def add_bit(a, b):
    if len(a) != len(b):
        return "Arrays must be of same size"
    results = [0 for i in range(len(a) + 1)]
    # work backwards, add and if it overflows then have a counter.
    extra = 0
    for i in range(len(a) - 1, -1, -1):
        if i == 0 and extra == 1:
            results[i] = 1
        sum = a[i] + b[i]
        results[i + 1] = sum + extra
        if results[i + 1] >= 2:
            results[i + 1] = results[i + 1] % 2
            extra = 1
        else:
            extra = 0
    return results


print(add_bit([0, 0, 0], [0, 0, 0]))
print(add_bit([0, 1, 1], [0, 1, 1]))
print(add_bit([1, 1, 1, 1],
              [1, 0, 1, 1]))
