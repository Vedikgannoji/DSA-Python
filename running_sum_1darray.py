#1480 Running sum of 1d Array sum(nums[0]…nums[i])
nums = [1,2,3,4]
def runningSum(nums):
    size=len(nums)
    res=[0]*size
    current_sum=0
    for i in range(0,size):
        res[i]=current_sum+nums[i]
        current_sum+=nums[i]
    return res
print(runningSum(nums))




                        