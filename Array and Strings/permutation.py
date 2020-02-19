#Given two strings, write a method to decide if one is a permutation of the other.
def permutation(str1,str2):
  totalchr=256
  check1=[0]*totalchr
  check2=[0]*totalchr
  if len(str1)!=len(str2):
    return False
  for i in str1:
    check1[ord(i)]+=1
  for i in str2:
    check2[ord(i)]+=1
  if check1==check2:
    return True
s1=input()
s2=input()
if permutation(s1,s2):
  print("YES")
else:
  print("NO")