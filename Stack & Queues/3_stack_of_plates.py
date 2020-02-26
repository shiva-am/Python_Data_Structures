class Stack:
    def __init__(self, value):
        self.stack = []
        self.sub_stack = []
        self.capacity = value
        self.i = len(self.stack) - 1
        self.count = 0
    def push(self, value):
        if len(self.sub_stack) < self.capacity:
            self.sub_stack.append(value)
        else:
            self.stack.append(self.sub_stack)
            self.sub_stack = []
            self.sub_stack.append(value)
    def print_stack(self):
          
    def pop(self):
        if len(self.sub_stack) > 0:
            self.sub_stack.pop()
        else:
            if self.count == self.capacity:
                self.i -= 1
                self.count = 0
            self.stack[self.i].pop()
            self.count += 1
s = Stack(5)
for i in range(23):
    s.push(i)
s.pop()
s.print_stack()