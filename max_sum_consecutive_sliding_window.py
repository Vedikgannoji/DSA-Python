nums = [4,2,1,7,8,1,2,8]
k=3
def cons_max_sum(nums,k): #not k-1 as slicing excludes end element
    sum_window=sum(nums[0:k])
    max_sum=sum_window
    for i in range(k,len(nums)):
        sum_window+=nums[i]
        sum_window-=nums[i-k]
        max_sum=max(max_sum,sum_window)
    return max_sum
print(cons_max_sum(nums,k))