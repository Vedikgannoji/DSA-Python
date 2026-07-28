#1480 Running sum of 1d Array sum(nums[0]…nums[i])
nums = [1,2,3,4]
def runningSum(nums):
    size=len(nums)
    res=[0]*size
    for i in range(0,size):
        for j in range(0,i+1):
            res[i]+=nums[j]
    return res
print(runningSum(nums))




                        