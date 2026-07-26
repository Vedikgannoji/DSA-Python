#Leetcode 1512 Number of Good Pairs Bruteforce
nums = [1,2,3,1,1,3]
def goodPairs(nums):
    res=0
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j] and i<j:
                res+=1
    return res
print(goodPairs(nums))