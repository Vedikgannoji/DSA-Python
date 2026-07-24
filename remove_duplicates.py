#remove duplicates from sorted array
nums = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(nums):
    read=1
    write=1
    while read<len(nums):
        if nums[read]!=nums[read-1]:
            nums[write]=nums[read]
            write+=1
        read+=1
    while write<len(nums):
        nums.remove[nums[write]]
        #use this when asked to remove duplicates completely

    return nums
    return nums[:write] #use this when asked just to return non-duplicates

print(remove_duplicates(nums))