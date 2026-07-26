#Leetcode 1512 Number of Good Pairs Bruteforce
nums = [1,2,3,1,1,3]
def goodPairs(nums):
    pairs=0
    seen={}
    for num in nums:
        if num in seen:
            pairs+=seen[num]
            seen[num]+=1
        else:
            seen[num]=1

    return pairs
    
print(goodPairs(nums))
