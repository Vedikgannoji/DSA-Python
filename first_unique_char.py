#First Unique Character in a String (LeetCode 387)
s = "loveleetcode"
def nonRepeating(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for i in range(0,len(s)):
        if freq[s[i]]==1:
            return i
    return -1

print(nonRepeating(s))