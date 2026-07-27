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

