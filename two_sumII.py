nums=[2,7,11,15]
target=9
def two_sumII(nums, target):
    left=0
    right=len(nums)-1
    while left<right:
        currect_sum=nums[left]+nums[right]
        if currect_sum==target:
            return [left+1,right+1]
        if currect_sum<target:
            left+=1
        else:
            right-=1
print(two_sumII(nums,target))