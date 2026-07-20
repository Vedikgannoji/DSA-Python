#basic
x=121
def palindrome(x):
    original=x
    rev=0
    while x>0:
        digit =x%10
        rev = rev*10 + digit
        x= x//10
    return rev==original

print(palindrome(x))

#optimised runtime
x=123
def palindrome(x):
    if x<0 or (x%10==0 and x!=0):
        return False
    rev=0
    while x>rev:
        rev= rev*10 + x%10
        x=x//10
    return rev==x or x==rev//10

print(palindrome(x))