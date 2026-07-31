#1768 Merge Strings Alternately
word1 = "ab"
word2 = "pqrs"
def mergeAlternatively(word1,word2):
    res=""
    limit=min(len(word1),len(word2))
    for i in range(limit):
        res+=word1[i]
        res+=word2[i]
    res+=word1[limit:]
    res+=word2[limit:]
    return res
    
print(mergeAlternatively(word1,word2))