#LeetCode 283
nums=[0,1,0,3,12]
def move_zeroes(nums):
    read=0
    write=0
    while read<len(nums):
        if nums[read]!=0:
            nums[write]=nums[read]
            write+=1
        read+=1
   
    return nums
print(move_zeroes(nums))


