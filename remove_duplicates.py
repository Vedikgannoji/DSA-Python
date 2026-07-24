#LeetCode 26 remove duplicates from sorted array
nums = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(nums):
    read=0
    write=0
    while read<len(nums):
        