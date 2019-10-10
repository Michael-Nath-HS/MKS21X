from math import floor

class Node:
    def __init__(self, v):
        self.data = v
        self.position = None

    def __str__(self):
        return "NODE WITH VALUE: %d" % self.data

class Pqueue:
    def __init__(self):
        self.listy = [None]

    def push(self, v):
        anode = Node(v)
        listy = self.listy

        if len(listy) == 1:
            anode.position = 1
            listy.append(anode)
            return

        listy.append(anode)
        anode.position = len(listy) - 1
        par = listy[floor(anode.position / 2)]

        def helper(arg):
            node = arg
            par = listy[floor(node.position / 2)]
            par.data, node.data = node.data, par.data
            node, par = par, node

            par = listy[floor(node.position / 2)]

            if par is None:
                return
            else:
                if par.data > node.data:
                    helper(node)

        if par.data > anode.data:
            helper(anode)

        return "Inserted %d" % v

    def tolist(self):
        queue = [x.data if x is not None else None for x in self.listy]
        if len(queue) > 1:
            return queue[1:]

    def peek(self):
        listy = self.listy
        if len(listy) == 1:
            return None
        return listy[1]

    def pop(self):
        listy = self.listy
        if len(listy) == 1:
            return None
        last = listy[-1]
        beg = listy[1]
        beg.data = last.data
        del listy[-1]

        node = listy[1]

        while 2 * node.position + 1 < len(listy) :
            
        try:
            kidL = listy[(2 * node.position)]
        except:
            kidL = None

        try:
            kidR = listy[(2 * node.position) + 1]
        except:
            kidR = None









heap = Pqueue()
print(heap.push(1))
print(heap.push(5))
print(heap.push(4))
print(heap.push(9))
print(heap.push(8))
print(heap.push(7))
print(heap.push(10))
print(heap.tolist())
print(heap.pop())
print(heap.tolist())
