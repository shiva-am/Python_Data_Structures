class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedlist:
  def __init__(self):
    self.head=None
  def insert(self,data):
    new_node=node(data)
    new_node.next=self.head
    self.head=new_node
  def reverse(self):
    prev=None
    cur=self.head
    while cur:
      nxt=cur.next
      cur.next=prev
      prev=cur
      cur=nxt
    self.head=prev
  def ispalindrome(self,p1,p2):
      while p1 is not None and p2 is not None:
        if p1.data!=p2.data:
          return False
        p1=p1.next
        p2=p2.next
      return True
  def printlist(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end="->")
            else:
                print(current.data)
            current = current.next
x=linkedlist()
y=linkedlist()
l=input()
for i in l[::-1]:
  x.insert(i)
  y.insert(i)
y.reverse()
if y.ispalindrome(x.head,y.head):
  print("Yes")
else:
  print("No")