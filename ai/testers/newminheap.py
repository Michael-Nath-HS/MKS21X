from math import floor

class Pqueue:
    def OriginalComparator(self, a, b):
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
        par = floor(cur / 2)

        # While the parent of our appended value is greater
        while self.cmpfunc(self, listy[par], listy[cur]) == 1 and listy[par] is not None:
            # Swap
            listy[par], listy[cur], cur = listy[cur], listy[par], par
            if floor(cur / 2) == 0:
                break
            else:
                par = floor(cur / 2)

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
        del(listy[-1])
        cur = 1
        rc = (2 * cur) + 1
        lc = 2 * cur

        while rc <= len(listy) - 1:
            if self.cmpfunc(self, listy[rc], listy[lc]) == 1 and self.cmpfunc(self, listy[lc], listy[cur]) == -1:
                listy[lc], listy[cur], cur = listy[cur], listy[lc], lc

            elif self.cmpfunc(self, listy[rc], listy[lc]) == -1 and self.cmpfunc(self, listy[rc], listy[cur]) == -1:
                listy[rc], listy[cur], cur = listy[cur], listy[rc], rc

            elif self.cmpfunc(self, listy[rc], listy[lc]) == 0:
                listy[lc], listy[cur], cur = listy[cur], listy[lc], lc

            rc = (2 * cur) + 1
            lc = 2 * cur
        try:
            if self.cmpfunc(self, listy[lc], listy[cur]) == -1:
                listy[lc], listy[cur] = listy[cur], listy[lc]

        except IndexError:
            return small












queue = Pqueue()
queue.push(17)
queue.push(15)
queue.push(10)
queue.push(10)
queue.push(12)
queue.push(6)
print(queue.tolist())
print(queue.pop())
print(queue.tolist())

def my_cmp(a,b):
    if len(a) > len(b):
        return 1
    if len(a) < len(b):
        return -1
    return 0