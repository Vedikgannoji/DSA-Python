def is_palindrome(s):
    l=0
    r=len(s)-1
    while l<r:
        while not s[l].isalnum():
            l+=1
            continue
        while not s[r].isalnum():
            r-=1
            continue
        while s[l].lower()!=s[r].lower():
            return False
        l+=1
        r-=1
    return True
            
s="A man, a plan, a canal: Panama"
print(is_palindrome(s))