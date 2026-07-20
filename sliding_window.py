nums=[1,2,3,4,5,6,7,8]
k=3 #window size

window_sum=sum(nums[:k])
print(window_sum)

maximum=window_sum
for i in range(k,len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i-k]

    maximum=max(maximum, window_sum)

print(maximum)