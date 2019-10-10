class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return "My value is : %d" % self.data
class MaxHeap:
    def __init__(self):
        self.root = None
        self.checker = False

    def insert(self, val):
        anode = Node(val)
        temp = self.root
        if self.root is None:
            self.root = anode
            return

        def helper(node,anode):
            while node.left is not None:
                node = node.left

            if node.left is None:
                node.left = anode
                anode.parent = node
                anode.parent, anode.parent.left, anode.parent.right, anode, anode.left, anode.right = anode, anode.left, anode.right, anode.parent, anode.parent.left, anode.parent.right
                self.checker = True
                return

            elif node.right is None:
                node.right = anode
                anode.parent = node
                anode.parent, anode.parent.left, anode.parent.right, anode, anode.left, anode.right = anode, anode.left, anode.right, anode.parent, anode.parent.left, anode.parent.right
                self.checker = True
                return "Inserted on Right"
            else:
                if self.checker:
                    return
                else:
                    helper(self.root.right,anode)
        helper(temp, anode)

heap = MaxHeap()
heap.insert(5)
heap.insert(3)