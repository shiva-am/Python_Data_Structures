#Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
def check(temp):
  row=[]
  col=[]
  for i in range(len(temp)):
    for j in range(len(temp)):
      if temp[i][j]==0:
        row.append(i)
        col.append(j)
  for i in range(len(temp)):
    for j in range(len(temp)):
      if i in row or j in col:
        temp[i][j]=0
  return temp
size=n=int(input())
matrix=[]
for i in range(size):
  temp=list(map(int,input().split()))
  matrix.append(temp)
print("\nZero Matrix :\n")
for i in (check(matrix)):
  print(*i)