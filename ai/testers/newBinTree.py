


class Node:
    def __init__(self, value=None):
        self.val = value
        self.parent = None
        self.smaller = None
        self.larger = None
        self.count = 1


class BinTree:
    def __init__(self, elements):
        self.root = None
        self.insert(elements[0])
        for i in elements:
            if not self.has(i):
                self.insert(i)

    def insert(self, v):
        v = Node(v)

        if self.root is None:
            self.root = v
            return

        def helper(node):
            if v.val > node.val:
                if node.larger is None:
                    node.larger = v
                    v.parent = node
                    return
                else:
                    helper(node.larger)

            elif v.val < node.val:
                if node.smaller is None:
                    node.smaller = v
                    v.parent = node
                    return
                else:
                    helper(node.smaller)

            elif v.val == node.val:
                node.count += v.count
                return

        return helper(self.root)

    def has(self, val):
        if not self.root:
            "Ok, You haven't even added anything..."
        cur = self.root
        while True:
            if cur.val == val:
                return True
            elif val > cur.val and (cur.larger is not None):
                cur = cur.larger
            elif val < cur.val and (cur.smaller is not None):
                cur = cur.smaller
            else:
                return False


    def get_ordered_list(self):
        ordered_list = []

        def helper(node):
            if node.smaller is not None:
                helper(node.smaller)
            for i in range(node.count):
                ordered_list.append(node.val)
            if node.larger is not None:
                helper(node.larger)

        helper(self.root)
        return ordered_list




tree = BinTree([1, 1, 2, 4, 2])
print(tree.get_ordered_list())