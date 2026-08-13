#27 Remove Element

nums = [0,1,2,2,3,0,4,2]
val = 2
def removeElement(nums,vale):
    res=[]
    for num in nums:
        if num!=val:
            res.append(num)
    return len(res)

print(removeElement(nums,val))    