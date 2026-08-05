#189 Rotate Array Optimised
nums = [1,2,3,4,5,6,7]
k = 3
def rotateArray(nums,k):
    k = k % len(nums)
    n=len(nums)
    def rotate(nums,i,j):
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    rotate(nums,0,n-1)
    rotate(nums,0,k-1)
    rotate(nums,k,n-1)

    return nums
print(rotateArray(nums,k))