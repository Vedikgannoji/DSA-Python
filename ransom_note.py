#Leetcode 383 Ransom Note
ransomNote = "aa"
magazine = "ab"

def ransom_note(ransomNote, magazine):
    if len(magazine)<len(ransomNote):
        return False
    freq={}
    for ch in magazine:
        freq[ch]=freq.get(ch,0)+1
    for ch in ransomNote:
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
                return False
    return True
print(ransom_note(ransomNote,magazine))
    