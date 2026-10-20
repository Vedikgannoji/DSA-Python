#2441 largest-positive-integer-that-exists-with-its-negative
nums = [-1,2,-3,3]
def largest_positive_integer_that_exists_its_negative(nums):
    res=-1
    seen=set(nums)
    for num in nums:
        if -(num) in seen:
            res=max(res,abs(num))
    return res
    
print(largest_positive_integer_that_exists_its_negative(nums))