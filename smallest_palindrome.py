str="babab"
def lexicographical(str):
    freq={}
    for ch in str:
        freq[ch]=freq.get(ch,0)+1
    left=""
    middle=""
    for ch in sorted(freq.keys()):
        left+=ch*(freq[ch]//2)
        if freq[ch]%2==0:
            middle=ch
    right=left[::-1]
    return left+middle+right
print(lexicographical(str))
