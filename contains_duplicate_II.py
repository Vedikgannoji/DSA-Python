# 129 Contains Duplicate II
nums = [1,2,3,1]
k = 3
def contains_duplicates(nums,k):
    last_index={}
    for i in range(0,len(nums)):
        if nums[i] in last_index:
            if i-last_index[nums[i]] <=k:
                return True
        last_index[nums[i]]=i
    return False

print(contains_duplicates(nums,k))
