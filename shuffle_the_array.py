#1470 Shuffle the array
nums = [2,5,1,3,4,7]
n = 3
def shuffleArray(nums,n):
    res=[]
    x=nums[0:n]
    for i in range(len(x)):
            res.append(x[i])
            res.append(nums[i+n])
    return res
print(shuffleArray(nums,n))
