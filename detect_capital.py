#520 Detect Capital 
word = "FlaG"
def detectCapital(word):
    return True if word.isupper() or word.islower() or word.istitle() else False
print(detectCapital(word))