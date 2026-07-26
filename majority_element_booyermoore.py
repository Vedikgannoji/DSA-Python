#Leetcode 169 Majority Element Booyer-Moore Algorithm
nums = [2,2,1,1,1,2,2]
def majority(nums):
    candidate=0
    count=0
    for num in nums:
        if count==0:
            candidate=num
            count+=1
        elif num==candidate:
            count+=1
        else:
            count-=1
    return candidate
print(majority(nums))
