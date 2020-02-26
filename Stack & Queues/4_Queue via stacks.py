class Queue:
  def __init__(self):
    self.stack1=[]
    self.stack2=[]
  def enqueue(self,val):
    self.stack1.append(val)
  def dequeue(self):
    while len(self.stack1)>0:
      p=self.stack1.pop()
      self.stack2.append(p)
    if len(self.stack2)==0:
      return "Queue is empty"
    return self.stack2.pop()
q=Queue()
values=list(map(int,input().split()))
for i in values:
  q.enqueue(i)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())