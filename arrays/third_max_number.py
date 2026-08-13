#414
nums = [3,2,1]
def thirdMaxNumber(nums):
    nums.sort()
    if len(nums)>=3:
        return nums[2]
    else:
        return nums[len(nums)]
print(thirdMaxNumber(nums))