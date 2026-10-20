#2248 intersection-of-multiple-arrays
nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
def intersection_of_multiple_arrays(nums):
    common=set(nums[0])
    for arr in nums:
        common=common.intersection(arr)
    return sorted(common)
print(intersection_of_multiple_arrays(nums))