#409 longest-palindrome
s = "abccccdd"
def longest_palindrome(s):
    freq={}
    longest=0
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for count in freq.values():
        longest+=(count//2)*2
    if len(s)!=longest:
        longest+=1
    return longest
print(longest_palindrome(s))