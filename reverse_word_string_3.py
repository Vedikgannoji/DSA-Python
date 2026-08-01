# 557 Reverse Words in a String III 
s = "Let's take LeetCode contest"
def reverseWords(s):
    new=s.split()
    res=""
    for word in new:
        res+=word[::-1]+" "
    return res.strip()

print(reverseWords(s))

#optimized one liner
def reverseWords2(s):
    return " ".join(word[::-1] for word in s.split())

print(reverseWords2(s))