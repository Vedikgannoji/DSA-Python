#Leetcode 242 Valid Anagram
s = "anagram"
t = "nagaram"
def anagram(s,t):
    res=True
    for i in range(0,len(s)):
        if s[i] not in t:
            res=False
    return res
print(anagram(s,t))
        