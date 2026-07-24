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

# Two Pointer Approach
# Compare absolute values at both ends.
# Place the larger square at the end of the answer array.
# Move the used pointer and continue until all elements are processed.
# TC: O(n) | SC: O(n)

nums = [-4,-1,0,3,10]
ans = [0] * len(nums)
def squares(nums):
    left=0
    right=len(nums)-1
    write=len(nums)-1
    while left<=right:
        if abs(nums[left])>abs(nums[right]):
            ans[write]=nums[left] ** 2
            left+=1
        else:
            ans[write]=nums[right] ** 2
            right-=1
        write-=1
    return ans
print(squares(nums))

