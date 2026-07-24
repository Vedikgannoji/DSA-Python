##Leetcode 977 Squares of a Sorted Array-without two pointers
nums = [-4,-1,0,3,10]
def squares(nums):
    res=[]
    for i in nums:
        res.append(i*i)
    res.sort()
    return res
print(squares(nums))
    