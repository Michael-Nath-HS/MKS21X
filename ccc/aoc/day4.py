
def day4():
    counter = 0
    for i in range(145852, 616943):
        adjacent = False
        smth = str(i)
        zoo = []
        for k in smth:
            zoo.append(int(k))

        if sorted(zoo) != zoo:
            continue
        nums = set()
        for j in range(len(zoo) - 1):
            z = j
            count = 0
            while zoo[z] == zoo[z + 1]:
                count += 1
                if z < len(zoo) - 1:
                    z += 1
            if count == 2:
                adjacent = True
                break
            zoo = zoo[z+1:]

        if adjacent:
            counter += 1

    return counter


print(day4())
