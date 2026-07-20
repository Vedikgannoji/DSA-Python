nums=[4,1,2,1,2]
def single_num(nums):
    seen= set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)


print(single_num(nums))