class Stack:
    def __init__(self):
        # inits an array implementation of stack
        self.arr = [None]
        # creates a top attribute that will keep track of
        # the last element of the stack
        self.top = 0

    def stack_empty(self):
        # checks to see if the stack is empty
        if self.top == 0:
            return True
        return False

    def push(self, x):
        # pushes an element to the end of a stack
        self.arr[self.top] = x
        self.top += 1

    def pop(self):
        if self.stack_empty():
            return "ERROR: STACK UNDERFLOW"
        self.top -= 1
        return self.arr[self.top + 1]

    def __repr__(self):
        return "{}".format(self.arr)
