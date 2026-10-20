#1002 find-common-characters
from collections import Counter
words = ["bella","label","roller"]
def find_common_characters(words):
    common=Counter(words[0])
    for word in words[1:]:
        freq=Counter(word)
        common &=freq
    return list(common.elements())
print(find_common_characters(words))