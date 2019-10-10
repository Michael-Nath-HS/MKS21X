from math import floor
class Node:
    def __init__(self, v):
        self.data = v
        self.position = None

    def __str__(self):
        return "NODE WITH VALUE: %d" % self.data

class MaxHeap:

    def __init__(self):
        self.listy = [None]



    def insert(self, v):
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
                if par.data < node.data:

                    helper(node)

        if par.data < anode.data:
            helper(anode)
            
        return "Inserted %d" % v


    def display(self):
        queue = [x.data if x is not None else None for x in self.listy]
        if len(queue) > 1:
            return queue[1:]

heap = MaxHeap()
print(heap.insert(2))
print(heap.insert(5))
print(heap.insert(7))
print(heap.insert(8))
print(heap.insert(2))
print(heap.insert(1))
print(heap.insert(2456))
print(heap.insert(98765456789))
print(heap.insert(3245))

print(heap.display())





