#Leetcode 242 Valid Anagram
'''s = "aa"
t = "a"
def anagram(s,t):
    if len(s)!=len(t):
        return False
    else:
        return sorted(s)==sorted(t)
print(anagram(s,t))'''
#without sorting method
s='aaa'
t='a'
def anagram(s,t):
    res=True
    if len(s)!=len(t):
            return False
    else:
        if len(s)>len(t):
            for i in range(0,len(s)):
                if s[i] not in t:
                    res=False
        else:
            for i in range(0,len(t)):
                if t[i] not in s:
                    res=False
    return res
print(anagram(s,t))


