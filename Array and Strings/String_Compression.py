#Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def check(word):
  output=""
  count=1
  for i in range(len(word)-1):
    if word[i+1]==word[i]:
      count+=1
    else:
      output+=word[i]+str(count)
      count=1
  output+=word[-1]+str(count)
  return output if len(output)<len(word) else word
string=input()
print(check(string))