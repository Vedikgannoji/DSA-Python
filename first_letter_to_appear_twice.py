# 2351 First letter to appear twice
def first_letter_to_appear_twice(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        if freq[ch] == 2:
            return ch
s = "abccbaacz"
print(first_letter_to_appear_twice(s))