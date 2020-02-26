class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class LinkedList:
  def __init__(self):
    self.ptr1 = None
    self.ptr2 = None
    self.dup = None
    self.head = None
  def push(self, new_data): 
    new_node = Node(new_data) 
    new_node.next = self.head 
    self.head = new_node 
  def remove_duplicates(self): 
    self.ptr1 = self.head
    while self.ptr1 != None and self.ptr1.next != None: 
      self.ptr2 = self.ptr1 
      while self.ptr2.next != None: 
        if self.ptr1.data == self.ptr2.next.data: 
          self.dup = self.ptr2.next 
          self.ptr2.next = self.ptr2.next.next 
        else: 
          self.ptr2 = self.ptr2.next
      self.ptr1 = self.ptr1.next
  def printList(self): 
    node = self.head
    while node != None: 
      print(str(node.data) + " ") 
      node = node.next
list = LinkedList()
input = [int(i) for i in input().split()]
for i in input[::-1]: 
  list.push(i) 
list.remove_duplicates()
list.printList()