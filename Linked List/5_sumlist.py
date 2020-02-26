class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedlist:
  def __init__(self):
    self.head=None
  def insert(self,val):
    new_node=node(val)
    new_node.next=self.head
    self.head=new_node
  def printl(self):
    cur=self.head
    while cur:
      if cur.next:
        print(cur.data,end="->")
      else:
        print(cur.data)
      cur=cur.next
  def reverse(self):
    prev=None
    cur=self.head
    while cur:
      nxt=cur.next
      cur.next=prev
      prev=cur
      cur=nxt
    self.head=prev
  def addtwonumbers(self,n1,n2):
    s=n1.data+n2.data
    self.head=node(s%10)
    result=self.head
    carry=int(s/10)
    l1=n1.next
    l2=n2.next
    while l1 is not None or l2 is not None:
        result.next=node((carry+l1.data+l2.data)%10)
        carry=int((carry+l1.data+l2.data)/10)
        l1=l1.next
        l2=l2.next
        result=result.next
    if carry>0:
      result.next=node(carry)
x=linkedlist()
y=linkedlist()
array1=[int(i) for i in input().split()]
for j in array1[::-1]:
  x.insert(j)
array2=[int(i) for i in input().split()]
for j in array2[::-1]:
  y.insert(j)
x.reverse()
y.reverse()
z=linkedlist()
z.addtwonumbers(x.head,y.head)
z.reverse()
z.printl()