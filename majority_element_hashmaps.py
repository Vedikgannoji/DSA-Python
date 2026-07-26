#Leetcode 169 Majority Element Hashmaps
nums = [2,2,1,1,1,2,2]
def majority(nums):
    m=(len(nums))/2
    seen={}
    for num in nums:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1
    for num in seen:
        if seen[num]>m:
            return num
print(majority(nums))
