#Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
def check(w):
  c=0
  for i in range(len(w)):
    bit=ord(w[i])-ord('a')
    if ((c&(1<<bit))>0):
      return False
    c=c|(1<<bit)
  return True
word=input()
if check(word):
  print("Word "+word+" has all unique characters")
else:
  print("Word "+word+" has duplicate characters")