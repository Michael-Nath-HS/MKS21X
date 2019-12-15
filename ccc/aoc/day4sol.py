import collections

def sol1():
    low = 145852
    high = 616943

    a1 = []
    a2 = []

    t = low

    while True:
        d = list(str(t))

        for i in range(5):
            if d[i] > d[i + 1]:
                d[i + 1:6] = d[i] * (5 - i)
                t = int("".join(d))
                d = list(str(t))
                break

        if t > high:
            break
        if (collections.Counter(str(t)).most_common(1)[0][1] > 1):
            a1.append(t)

        if (2 in collections.Counter(str(t)).values()):
            a2.append(t)

        t += 1
    return set(a1)



def day4():
    adjacent = False
    counter = []
    for i in range(145852, 616943):
        smth = str(i)
        zoo = []
        for k in smth:
            zoo.append(int(k))


        # if int(track) in container:
        #     continue
        # print(container)
        # container.add(int(track))

        if sorted(zoo) != zoo:
            continue

        for j in range(len(zoo) - 1):
            if zoo[j] == zoo[j+1]:
                adjacent = True
                break

        if adjacent:
            # print(i)
            counter.append(i)

    return set(counter)


b = sol1()
c = day4()

print(c.difference(b))