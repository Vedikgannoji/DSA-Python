#2114 Maximum Number of Words Found in Sentences
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
def maxWords(sentences):
    max_words=0
    for sentence in sentences:
        count=1
        for ch in sentence:
            if ch==" ":
                count+=1
        max_words=max(max_words,count)
    return max_words
        
print(maxWords(sentences))

#short
def maxWords2(sentences):
    return max(len(sentence.split()) for sentence in sentences)
        
print(maxWords2(sentences))