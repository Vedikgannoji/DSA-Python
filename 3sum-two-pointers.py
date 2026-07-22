# optimised 3 sum using two pointers(opp direction)
nums=[-1,0,1,2,-1,-4]
target=0
def threeSum(nums,target):
    nums.sort()
    res=[]

    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while left<right:
            total = nums[i]+ nums[left] + nums[right]
            if total<target:
                left+=1
            elif total>target:
                right-=1
            else:
                res.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1

                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
    return res
print(threeSum(nums,target))