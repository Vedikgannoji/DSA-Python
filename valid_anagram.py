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
    if len(s) != len(t):
        return False
    set_s = set(s)
    for i in set_s:
        if s.count(i) != t.count(i):
            return False
    return True
print(anagram(s,t))


