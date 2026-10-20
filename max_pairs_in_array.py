#2341 maximum-number-of-pairs-in-array
nums = [1,3,2,1,3,2,2]
def max_no_pairs_array(nums):
    freq={}
    for num in nums:
        freq[num]= freq.get(num,0)+1
    pairs=0
    leftover=0
    for count in freq.values():
        pairs+=count//2
        leftover+=count%2
    return [pairs,leftover]
print(max_no_pairs_array(nums))