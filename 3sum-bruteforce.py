#3 sum
#brute-force
nums=[-1,0,1,2,-1,-4]
target=0
end=len(nums)-1
def three_sum(nums, target):
    for i in range(0,end):
        for j in range(1,end):
            for k in range(2, end):
                if nums[i]+nums[j]+nums[3]==target:
                    return [i,j,k]
print(three_sum(nums,target))

#time complexity=O(nxnxn)=O(n^3)