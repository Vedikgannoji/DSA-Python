#290 Word Pattern
pattern = "abba"
s = "dog cat cat dog"
def wordPattern(pattern: str, s: str) -> bool:
    pattern_to_word={}
    word_to_pattern={}
    words=s.split()
    for p,w in zip(pattern,words):
        if p in pattern_to_word:
            if pattern_to_word[p]!=w:
                return False
        else:
            pattern_to_word[p]=w
        if w in word_to_pattern:
            if word_to_pattern[w]!=p:
                return False
        else:
            word_to_pattern[w]=p
    return True

print(wordPattern(pattern,s))