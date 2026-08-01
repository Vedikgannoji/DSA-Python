#1221 Split a String in Balanced Strings 
s = "RLRRLLRLRL"
def splitString(s):
    count=0
    r=0
    l=0
    for ch in range(0,len(s)):
        if s[ch]=='R':
            r+=1
        else:
            l+=1
        if r!=0 and l!=0 and r==l:
            count+=1
            r=0
            l=0
        
    return count

print(splitString(s))