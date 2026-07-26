#Leetocde 268 Missing Number optimised
nums = [9,6,4,2,3,5,7,0,1]
def missing_num(nums):
    n=len(nums)
    return int(((n*(n+1))/2)-sum(nums))
print(missing_num(nums))