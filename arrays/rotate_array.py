#189 Rotate Array
nums = [1,2,3,4,5,6,7]
k = 3
def rotateArray(nums,k):
    i=0
    j=len(nums)-1
    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    i=0
    j=k-1
    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    i=k
    j=len(nums)-1
    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    
    return nums
print(rotateArray(nums,k))