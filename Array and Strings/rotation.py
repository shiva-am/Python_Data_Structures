#Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. can you do this in place?
class rotate:
  def rotate90degree(temp1):
    for i in range(len(temp1)):
      k=len(temp1)-1
      for j in range(len(temp1)):
        temp1[i][j]=temp1[k][i]
        k-=1
    return temp1
matrix_size=int(input())
matrix=[]
for i in range(matrix_size):
  temp=input().split()
  matrix.append(temp)
t=rotate
print("\nAfter rotation:\n")
for i in (t.rotate90degree(matrix)):
  print(*i)
