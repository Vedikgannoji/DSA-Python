#Leetcode 1464 Maximum Product of two elements in an array
nums = [3,4,5,2]
def maxProduct(nums):
    first,second=0,0
    for num in nums:
        if num>first:
            second=first
            first=num
        elif num>second:
            second=num
    return ((first-1)*(second-1))
print(maxProduct(nums))
#optimised
def maxProduct2(nums):
    nums.sort()
    return ((nums[-1]-1)*(nums[-2]-1)) 
print(maxProduct2(nums))
#bruteforce
def maxProduct3(nums):
    res=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            current=(nums[i]-1)*(nums[j]-1)
            res=max(res,current)
    return res
print(maxProduct3(nums))
