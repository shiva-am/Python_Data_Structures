#Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
class check:
    def isequal(s1,s2):
      return set(s1)==set(s2)
string1=input()
string2=input()
t=check
print("Two words are same." if t.isequal(string1,string2) else "Two words are not same.")