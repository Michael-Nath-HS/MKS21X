class Node:
    def __init__(self, value=None):
        self.val = value
        self.parent = None
        self.smaller = None
        self.larger = None
        self.count = 1

class BinTree:
    def __init__(self):
        self.root = None

    def insert(self, v):
        v = Node(v)
        if self.root == None:
            self.root = v
            return

        def helper(node):
            if v.val > node.val:
                if node.larger is None:
                    node.larger = v
                else:
                    helper(node.larger)
            elif v.val < node.val:
                if node.smaller is None:
                    node.smaller = v
                else:
                    helper(node.larger)

            elif v.val == node.val:
                node.count += v.count

            # elif v.val == node.val:
                # if v.val % 2 == 1:
                #     helper(node.smaller)
                # else:
                #     helper(node.larger)

            # # elif v.val == node.val:
            #     if (node.larger != None) and (node.smaller == None):
            #         node.smaller = v
            #     elif (node.larger == None) and (node.smaller != None):
            #         node.larger = v

        return helper(self.root)

    def isThere(self, val):

        if self.root == None:
            "Ok, You haven't even added anything..."
        cur = self.root
        while True:
            if cur.val == val:
                print(cur.smaller.val)
                return "Yes this exists in the tree"
            elif val > cur.val and (cur.larger != None):
                cur = cur.larger
            elif val < cur.val and (cur.smaller != None):
                cur = cur.smaller
            else:
                return "This doesn't exist chief"

    def display(self):
        l = []
        def helper(node):
            if node.smaller != None:
                helper(node.smaller)
            for i in range(node.count):
                l.append(node.val)
            if node.larger != None:
                helper(node.larger)
        helper(self.root)
        return l


tree = BinTree()
tree.insert(5)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(2)
# print(tree.isThere(7))
# print(tree.isThere(6))
# print(tree.isThere(5))
print(tree.display())





