#1768 Merge Strings Alternately
word1 = "ab"
word2 = "pqrs"
def mergeAlternatively(word1,word2):
    res=""
    new=""
    w1=len(word1)
    w2=len(word2)
    maxw=word1 if w1>w2 else word2
    minw=word1 if w1<w2 else word2

    if w1!=w2:
        new=maxw[len(minw):]
    for i in range(len(w)):
        res+=(minw[i]+maxw[i])
    
    return res+new
    
print(mergeAlternatively(word1,word2))