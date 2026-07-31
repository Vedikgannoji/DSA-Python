#58 Length of Last Word
s = "Hello World"
def lengthLastWord(s):
    count=0
    for ch in range(len(s)-1,-1,-1):
        if s[ch]!=" ":
            count+=1
        else:
            break
    return count

print(lengthLastWord(s))