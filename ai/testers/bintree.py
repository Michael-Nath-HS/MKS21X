class node:
    def __init__(self, val):
        self.value = val
        self.par = None
        self.small = None
        self.great = None

class bintree:

    def __init__(self):
        self.root = None

    def append(self, value):
        anode = node(value)
        if self.root == None:
            self.root = anode
        else:
            cur = self.root
            while True:
                if (anode.value < cur.value) and (cur.small == None):
                    cur.small = anode
                    anode.par = cur
                    return
                if (anode.value > cur.value) and (cur.great == None):
                    cur.great = anode
                    anode.par = cur
                    return
                if (anode.value > cur.value) and (cur.great != None):
                    cur = cur.great
                if (anode.value < cur.value) and (cur.small != None):
                    cur = cur.small

    def isThere(self, val):
        if self.root == None:
            "Ok, You haven't even added anything..."

        cur = self.root
        while True:
            if cur.value == val:
                return "Yes this exists in the tree"
            elif val > cur.value and (cur.great != None):
                cur = cur.great
            elif val < cur.value and (cur.small != None):
                cur = cur.small
            else:
                return "This doesn't exist chief"
    def display(self):
        l = []
        def helper(node):
            if node.small != None:
                helper(node.small)
            l.append(node.value)
            if node.great != None:
                helper(node.great)

        helper(self.root)
        return l



mytree = bintree()
mytree.append(3)
mytree.append(5)
mytree.append(2)
mytree.append(17)
mytree.append(0)
print(mytree.display())
