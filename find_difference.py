#389 Find the Difference 
s = "abcd"
t = "abcde"
def difference(s,t):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1

    for ch in t:
        freq[ch]=freq.get(ch,0)-1
        if freq[ch]<0:
            return ch

print(difference(s,t))
