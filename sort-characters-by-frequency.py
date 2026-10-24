#451 sort-characters-by-frequency
s = "tree"
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