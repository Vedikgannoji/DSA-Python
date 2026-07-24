#Leetcode 977 Squares of a Sorted Array
#bruteforce-O(nlogn) tc
#squaring-O(n) Sorting O(nlogn)
'''
nums = [-4,-1,0,3,10]
def squares(nums):
    read=0
    write=0
    while read<len(nums):
        nums[write]=(nums[read]**2)
        write+=1
        read+=1
    nums.sort()
    return nums
print(squares(nums))
'''
#optimized
nums = [-4,-1,0,3,10]
def squares(nums):
    

