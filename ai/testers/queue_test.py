#! /usr/bin/python3

class Pqueue:
    def OriginalComparator(a, b):
        if a < b:
            return -1
        if a == b:
            return 0
        return 1

    def __init__(self, comparator=OriginalComparator):
        self.cmpfunc = comparator
        self.listy = [None]

    def push(self, data):
        listy = self.listy
        # If there are no real data in queue, just append it
        if len(listy) == 1:
            listy.append(data)
            return

        # Append the data to very end; Bubble it up so it satisfies the min pqueue
        listy.append(data)
        cur = len(listy) - 1
        par = cur // 2

        # While the parent of our appended value is greater
        while self.cmpfunc(listy[par], listy[cur]) == 1 and listy[par] is not None:
            # Swap
            listy[par], listy[cur], cur = listy[cur], listy[par], par
            if cur // 2 == 0:
                break
            else:
                par = cur // 2

        self.listy = listy
        return

    def tolist(self):
        return self.listy[1:]

    def pop(self):
        listy = self.listy

        if len(listy) == 1:
            return None
        if len(listy) == 2:
            return listy.pop()

        small = listy[1]
        listy[1] = listy[-1]
        del (listy[-1])
        cur = 1
        rc = (2 * cur) + 1
        lc = 2 * cur

        while rc <= len(listy) - 1:
            if self.cmpfunc(listy[rc], listy[lc]) == 1 and self.cmpfunc(listy[lc], listy[cur]) == -1:
                listy[lc], listy[cur], cur = listy[cur], listy[lc], lc

            elif self.cmpfunc(listy[rc], listy[lc]) == -1 and self.cmpfunc(listy[rc], listy[cur]) == -1:
                listy[rc], listy[cur], cur = listy[cur], listy[rc], rc

            elif self.cmpfunc(listy[rc], listy[lc]) == 0:
                listy[lc], listy[cur], cur = listy[cur], listy[lc], lc

            rc = (2 * cur) + 1
            lc = 2 * cur
        try:
            if self.cmpfunc(listy[lc], listy[cur]) == -1:
                listy[lc], listy[cur] = listy[cur], listy[lc]

        except IndexError:
            return small
        return small


def compare(a, b):
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1

    elif len(a) == len(b):
        a = a.lower()
        b = b.lower()
        if a > b:
            return 1
        if a == b:
            return 0
        return -1


def tester():
    import sys
    queue = Pqueue(compare)

    try:
        inpt = open(sys.argv[1], "r", encoding='utf-8-sig')
        outpt = open(sys.argv[2], "w")
    except ValueError:
        return "Not valid file types."

    read_in = inpt.read().split("\n")

    for i in read_in:
        i = i.strip()
        i = i.split(" ")
        print(i)

        if i[0] == "push":
            queue.push("{}".format(i[1]))
        elif i[0] == "pop":
            queue.pop()

        if i[0] == "tolist":
            ordered_list = []
            for k in range(len(queue.tolist())):
                ordered_list.append(queue.pop())

            outpt.write("{}".format(",".join(ordered_list)))


tester()
