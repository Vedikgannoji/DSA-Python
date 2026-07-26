#Leetocde 268 Missing Number using Hashmaps
nums = [9,6,4,2,3,5,7,0,1]
def missing_num(nums):
    stored=set(nums)
    for i in range(0,len(stored)+1):
        if i not in stored:
            return i
print(missing_num(nums))