#First Unique Character in a String (LeetCode 387)
s = "loveleetcode"
def nonRepeating(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch in s:
        if freq[ch]==1:
            return s.index(ch)
    return -1

print(nonRepeating(s))