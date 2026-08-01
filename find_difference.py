#389 Find the Difference 
s = "abcd"
t = "abcde"
def difference(s,t):
    for ch in t:
        if ch not in s:
            return ch

print(difference(s,t))
