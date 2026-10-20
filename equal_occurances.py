#1941 check-if-all-characters-have-equal-number-of-occurrences
s = "abacbc"
def equal_occurances(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0) + 1
    if len(set(freq.values()))==1:
        return True 
    else:
        return False
print(equal_occurances(s))
    