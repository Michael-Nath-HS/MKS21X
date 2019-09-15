class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        cur_index = 0
        cur_node = self.head
        if index >= self.length():
            return "Yah this index too much"

        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            else:
                cur_index += 1
    def erase(self,index):
        cur_index = 0
        cur_node = self.head
        if index >= self.length():
            return "Yah this index too much"

        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                # [3,4,5,6]
                return
            cur_index += 1




my_linked_list = linked_list()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.display()
print("Index at 2: %d" % my_linked_list.get(0))