#128 longest-consecutive-sequence
nums = [100,4,200,1,3,2]
def longest_consecutive_sequence(nums):
    num_set=set(nums)
    longest=0
    for num in num_set:
        if num-1 not in num_set:
            count=1
            current=num
            while current + 1 in num_set:
                count+=1
                current+=1
            longest=max(longest,count)
    return longest
print(longest_consecutive_sequence(nums))