#451 sort-characters-by-frequency
s = "tree"
from collections import Counter
def sort_characters_by_frequency(s):
    freq={}
    res=''
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    sorted_s=sorted(freq,key=lambda ch:freq[ch],reverse=True)
    for ch in sorted_s:
        res+=ch*freq[ch]
    return res
print(sort_characters_by_frequency(s))

def sort_characters_by_frequency2(s):
    c=Counter(s)
    s2=sorted(c.keys(),key=lambda x:c[x], reverse=True)
    return "".join(x*c[x] for x in s2)
print(sort_characters_by_frequency2(s))
