#There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
def One_away(word1,word2):
    w1len=len(word1)
    w2len=len(word2)
    if(abs(w1len-w2len)>1):
        return False
    count=0
    w1ind=0
    w2ind=0
    while(w1ind<w1len and w2ind<w2len):
        if(word1[w1ind]!=word2[w2ind]):
            if(count>1):
                return False
            if w1len<w2len:
                w1ind+=1
            elif w2len<w1len:
                w2ind+=1
            else:
                w1ind+=1
                w2ind+=1
            count+=1
        else:
            w1ind+=1
            w2ind+=1
    if(w1ind<w1len or w2ind<w2len):
        count+=1 
    return count==1
word1,word2=input().split()
if(One_away(word1,word2)):
    print('Yes they are one edit away')
else:
    print('No they have more than one edit')

