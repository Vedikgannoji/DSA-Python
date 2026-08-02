#14 Longest Common Prefix 

strs = ["flower","flow","flight"]
def longestCommonPrefix(strs):
    prefix=""
    n=len(min(strs,key=len))
    for i in range(0,n):
            for word in strs:
                if word[i]!=strs[0][i]:
                    return prefix
            prefix+=strs[0][i]
    return prefix
print(longestCommonPrefix(strs))
