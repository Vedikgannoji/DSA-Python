#414
nums = [3,2,1]
def thirdMaxNumber(nums):
    n = sorted(set(nums))

    if len(n) >= 3:
        return n[-3]
    else:
        return n[-1]
print(thirdMaxNumber(nums))