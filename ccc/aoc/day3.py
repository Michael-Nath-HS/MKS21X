

def solver(direction, x, y):
    if direction[0] == "R":
        coord = [[i, y] for i in range(x, int(direction[1:]) + 1)]
        x += int(direction[1:])
    elif direction[0] == "L":
        coord = [[i, y] for i in range(x, x - (int(direction[1:]) + 1), -1)]
        x -= int(direction[1:])
    elif direction[0] == "U":
        coord = [[x, i] for i in range(y, int(direction[1:]) + 1)]
        y += int(direction[1:])
    elif direction[0] == "D":
        coord = [[x, i] for i in range(y, y - (int(direction[1:]) + 1), -1)]
        y -= int(direction[1:])

    print("x is {}".format(x))

    return coord

# print(solver("D6"))
# print(solver("U6"))
# print(solver("R6"))
# print(solver("L6"))



def part1():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    storage1 = []
    storage2 = []
    both = []
    inpt = open("day3.in", "r").read().split("\n")
    wire1 = "".join(inpt[0].split()).split(",")
    wire2 =  "".join(inpt[1].split()).split(",")
    for i in wire1:
        if i[0] == "R":
            coord = [[j, y1] for j in range(x1, x1 + int(i[1:]) + 1)]
            x1 += int(i[1:])
        elif i[0] == "L":
            coord = [[j, y1] for j in range(x1, x1 - (int(i[1:]) + 1), -1)]
            x1 -= int(i[1:])
        elif i[0] == "U":
            coord = [[x1, j] for j in range(y1, y1 + int(i[1:]) + 1)]
            y1 += int(i[1:])
        elif i[0] == "D":
            coord = [[x1, j] for j in range(y1, y1 - (int(i[1:]) + 1), -1)]
            y1 -= int(i[1:])
        for z in coord:
            storage1.append(z)

    for i in wire2:
        if i[0] == "R":
            coord = [[j, y2] for j in range(x2, x2 + int(i[1:]) + 1)]
            x2 += int(i[1:])
        elif i[0] == "L":
            coord = [[j, y2] for j in range(x2, x2 - (int(i[1:]) + 1), -1)]
            x2 -= int(i[1:])
        elif i[0] == "U":
            coord = [[x2, j] for j in range(y2, y2 + int(i[1:]) + 1)]
            y2 += int(i[1:])
        elif i[0] == "D":
            coord = [[x2, j] for j in range(y2, y2 - (int(i[1:]) + 1), -1)]
            y2 -= int(i[1:])
        print(coord)
        for z in coord:
            if z in storage1:
                both.append(z)
            # storage2.append(z)

    # print(storage1)


    # print("\n")
    # print(both)
    # print(x1)
    # print(x2)
    # print(y1)
    # print(y2)



part1()