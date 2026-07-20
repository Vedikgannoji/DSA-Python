def single_num(nums):
    ans=0
    for num in nums:
        ans^=num
    return ans
nums=[4,1,2,1,2]
print(single_num(nums))