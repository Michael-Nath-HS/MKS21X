class Node:
    #Init object
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return "NODE VALUE: %d" % self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self): # Prints contents of a linked list
        # Sets the first node as the node to start traversing
        temp = self.head
        # will loop until hits a None
        while temp:
            print(temp.data)
            # Change the node to the next node
            temp = temp.next

    def insertfront(self, value):
        anode = Node(value)
        anode.next = self.head
        self.head = anode

    def insertend(self,value):
        anode = Node(value)
        if self.head is None:
            self.head = anode
            return
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = anode
                return
            else:
                temp = temp.next

    def insertafter(self, prevnode, value):
        if prevnode is None:
            return "Previous Node has to be in linked list"

        anode = Node(value)
        anode.next = prevnode.next
        prevnode.next = anode

    def delete(self,value):
        anode = Node(value)
        temp = self.head

        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return "Cannot delete. Key not in linked list"

        prev.next = temp.next
        temp = None

    def deletelist(self):
        cur = self.head

        while cur:
            prev = cur.next
            del(cur.data)
            cur = prev

    def length(self):
        lengthy = []
        cur = self.head
        if cur.data is None:
            return 0
        def helper(node):
            if node is not None:
                lengthy.append(1)
                helper(node.next)
            else:
                return
        helper(cur)
        return len(lengthy)

linked = LinkedList()
linked.head = Node(1)
second = Node(2)
third = Node(3)
# Links the first node to the second
linked.head.next = second
# Links the second node to the third
second.next = third
# adds a node to the front of a linked list
linked.insertend(8)
linked.insertend(9)
linked.insertafter(third, 57)
# linked.printlist()
linked.delete(8)
print("New List:")
linked.printlist()
print(linked.length())
