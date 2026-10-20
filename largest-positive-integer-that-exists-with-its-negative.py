#2441 largest-positive-integer-that-exists-with-its-negative
nums = [-1,2,-3,3]
def largest_positive_integer_that_exists_its_negative(nums):
    res=[]
    for num in nums:
        if abs(num) in nums:
            res.append(abs(num))
    if not res:
        return -1
    else:
        return max(res)
print(largest_positive_integer_that_exists_its_negative(nums))