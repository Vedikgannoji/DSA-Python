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

#using join- use a list initially and join as string for output as strings are immutable and create a new string for every operation.
def mergeAlternatively2(word1,word2):
    res=[]
    limit=min(len(word1),len(word2))
    for i in range(limit):
        res.append(word1[i])
        res.append(word2[i])
    res.append(word1[limit:])
    res.append(word2[limit:])
    return "".join(res)
print(mergeAlternatively2(word1,word2))