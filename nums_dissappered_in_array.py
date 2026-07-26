#Leetcode 448 Find All Numbers Disappeared in an Array
nums = [4,3,2,7,8,2,3,1]
def nums_disppeared(nums):
    res=[]
    current_nos=set(nums)
    for num in range(1,len(nums)+1):
            if num not in current_nos:
                res.append(num)
    return res
print(nums_disppeared(nums))