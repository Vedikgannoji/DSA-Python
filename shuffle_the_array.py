#1470 Shuffle the array
nums = [2,5,1,3,4,7]
n = 3
def shuffleArray(nums,n):
    res=[]
    for i in range(0,3):
            res.append(nums[i])
            res.append(nums[i+n])
    return res
print(shuffleArray(nums,n))
