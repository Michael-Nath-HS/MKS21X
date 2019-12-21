from math import sqrt


def distance(p1x, p1y, p2x, p2y):
    return sqrt(((p1x - p2x) ** 2) + ((p1y - p2y) ** 2))


assert distance(0, 0, 5, 5) == sqrt(50)


def solver(bname):
    inpt = open("points.csv", "r")
    oupt = open("output.csv", "a")
    sets = inpt.read().split("\n\n")
    xcor = False
    ycor = True
    points = []
    stack = dict()
    routes = dict()
    for i in sets:
        if i.split("\n")[0].split(",")[0] == bname:
            dist = i.split("\n")[0].split(",")[1]
            xcor = i.split("\n")[1].split(",")
            ycor = i.split("\n")[2].split(",")

    for i in range(len(xcor)):
        points.append((int(xcor[i]), int(ycor[i])))
        routes[(int(xcor[i]), int(ycor[i]))] = i

    stack[points[0]] = 0
    cur = points[0]

    def helper(stack, cur):
        dists = {}
        for j in points:
            if j not in stack.keys():
                dists[distance(cur[0], cur[1], j[0], j[1])] = j
        if len(dists.keys()) == 0 or len(stack) == len(points):
            return

        stack[dists[min(dists.keys())]] = min(dists.keys())
        cur = list(stack.keys())[-1]
        helper(stack, cur)

    helper(stack, cur)

    org = list(stack.keys())[0]
    stack[org] = distance(org[0], org[1], list(stack.keys())[-1][0], list(stack.keys())[-1][-1])
    length = sum(stack.values())
    overall = stack
    for j in points:
        chooser = {j: 0}
        helper(chooser, j)
        org = list(chooser.keys())[0]
        chooser[org] = distance(org[0], org[1], list(chooser.keys())[-1][0], list(chooser.keys())[-1][-1])
        if sum(chooser.values()) < length:
            overall = chooser
    ans = [str(routes[i]) for i in overall.keys()]
    oupt.write(bname + "\n")
    oupt.write(",".join(ans))
    oupt.write("\n\n")
    print(sum(overall.values()))


solver("A4")
solver("A8")
solver("A9")
solver("A9-2")
solver("A10")
solver("A11")
solver("A12")
solver("A12-2")
solver("A13")
solver("A13-2")
solver("A30")
solver("A50")
