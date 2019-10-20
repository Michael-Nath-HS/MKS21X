def normal_compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0

    return -1

class MaxHeap:
    def __init__(self, cmp = normal_compare):
        self.compare = normal_compare
        self.listy = [None]

    def push(self,data):
        listy = self.listy
        if len(listy) == 1:
            listy.append(data)
            print("Done!")
            return
        listy.append(data)
        cur = len(listy) - 1

        while listy[cur // 2] is not None:
            if self.compare(listy[cur // 2], listy[cur]) == -1:
                listy[cur // 2], listy[cur] = listy[cur], listy[cur // 2],
                cur = cur // 2
            else:
                break
        return

    def pop(self):
        listy = self.listy
        if len(listy) == 1:
            return None
        if len(listy) == 2:
            return listy.pop()

        beg = listy[-1]
        listy[1], listy[-1] = listy[-1], listy[1]
        del(listy[-1])
        cur = 1
        rc = (2 * cur) + 1
        lc = 2 * cur
        while rc <= len(listy) - 1:
            if self.compare(listy[rc], listy[lc]) == 1 and self.compare(listy[rc], listy[cur]) == 1:
                listy[rc], listy[cur], cur = listy[cur], listy[rc], rc

            elif self.compare(listy[rc], listy[lc]) == -1 and self.compare(listy[lc], listy[cur]) == 1:
                listy[lc], listy[cur], cur = listy[cur], listy[lc], lc

            elif self.compare(listy[rc], listy[lc]) == 0:
                listy[lc], listy[cur], cur = listy[cur], listy[lc], lc

            rc = (2 * cur) + 1
            lc = 2 * cur

        try:
            if self.compare(self, listy[lc], listy[cur]) == 1:
                listy[lc], listy[cur] = listy[cur], listy[lc]

        except IndexError:
            return beg


    def display(self):
        if len(self.listy) == 1:
            return "Nothing here: {}".format([])
        return self.listy[1:]


heap = MaxHeap()
heap.push(1)
heap.push(7)
heap.push(4)
heap.push(23)
heap.push(464)
heap.push(3)
print(heap.display())
heap.pop()
print(heap.display())