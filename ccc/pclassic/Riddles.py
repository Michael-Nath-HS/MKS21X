def solver(instructs):
    pos = set()
    neg = set()
    for i in instructs:
        # x1 = i[0]
        # x2 = i[1]
        pos.add(i) if i > 0 else neg.add(i)
    pos = list(pos)

    for elem in pos:
        if elem * -1 not in neg:
            return True

    return False


print(solver([-1,2, 2,-3, 3,-4 ,4,5, 5,-4,5,6, 6,-7 ,7,8, 8,1 ,1,-8, 8,-2, 2,8, 2,3, 3,8, 8,-3, 8,4, 4,2, 4,-1 -4,-1]))
