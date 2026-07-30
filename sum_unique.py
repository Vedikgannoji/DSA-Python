#Leetcode 1748 Sum of Unique elements
nums=[1,2,3,2]
def sumUnique(nums):
    freq={}
    total=0
    for num in nums:
        freq[num]=freq.get(num,0)+1
    for num,count in freq.items():
        if count==1:
            toal+=num
    return sum(new)
print(sumUnique(nums))