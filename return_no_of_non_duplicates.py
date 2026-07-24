#leetcode 26-return nu. of non duplicates from sorted array containing duplicates
nums = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(nums):
    read=1
    write=1
    while read<len(nums):
        if nums[read]!=nums[read-1]:
            nums[write]=nums[read]
            write+=1
        read+=1
    return write

print(remove_duplicates(nums))