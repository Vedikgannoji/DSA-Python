
#basic
nums=[2,7,11,15]
target=9

def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
result = twosum(nums,target)
print(result)

#using hashmaps
nums=[3,2,4]
target=6
def twosum(nums,target):
    prev_visited={}
    for i, num in enumerate(nums):
        diff=target-num
        if diff in prev_visited:
            return [prev_visited[diff],i]
        prev_visited[num]=i
result = twosum(nums,target)
print(result)       
    