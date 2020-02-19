#Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
def check(word):
  totalchr=256
  c=0
  temp=[0]*totalchr
  for i in word:
    temp[ord(i)]+=1
  for i in temp:
    if (i & 1):
      c+=1
    if c>1:
      return False
  return True
string=input()
if check(string):
  print("YES")
else:
  print("NO")