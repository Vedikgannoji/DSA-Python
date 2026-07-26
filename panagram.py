#Leetcode 1832 Check if the Sentence Is a Pangram
sentence = "thequickbrownfoxjumpsoverthelazydog"
def panagram(sentence):
    if len(set(sentence)) !=26:
        return False
    else:
        return True
print(panagram(sentence))
