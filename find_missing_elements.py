#3731 Find Missing Elements
nums = [1,5]
def findMissing(nums):
    res=[]
    for num in range(min(nums),max(nums)):
        if num not in nums:
            res.append(num)

    return res
print(findMissing(nums))
