#58 Length of Last Word
s = "Hello World"
def lengthLastWord(s):
    count=0
    started=False #to ensuure code works if space is at the end
    for ch in range(len(s)-1,-1,-1):
        if s[ch]==" ":
            if started:
                break
        else:
            started=True
            count+=1
    return count

print(lengthLastWord(s))