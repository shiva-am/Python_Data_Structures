class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end="->")
            else:
                print(current.data)
            current = current.next
    def partition(self, x):
        current = self.head
        before = Node(0)
        after = Node(0)
        before_head = before
        after_head = after
        print(before_head.data)
        while current:
            if current.data < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
            after.next = None
        before.next = after_head.next
        self.head = before_head.next
x = LinkedList()
array = [int(number) for number in input().split()]
partition_value = int(input())
for i in array[::-1]:
    x.insert(i)
x.partition(partition_value)
x.printlist()
