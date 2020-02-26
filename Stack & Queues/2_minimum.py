class stack:
  def __init__(self):
    self.stack=[]
    self.min=0
  def push(self,val):
    if len(self.stack)==0:
      self.stack.append(val)
      self.min=val
    else:
      self.stack.append(val)
      if val<self.min:
        self.min=val
  def minimum(self):
    return self.min
num=list(map(int,input().split()))
s=stack()
for i in num:
  s.push(i)
print(s.minimum())