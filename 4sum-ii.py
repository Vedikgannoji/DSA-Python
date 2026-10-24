#454 4sum-ii
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
def four_sum2(nums1, nums2, nums3, nums4):
    count=0
    freq1={}
    for n1 in nums1:
        for n2 in nums2:
            n=n1+n2
            freq1[n]=freq1.get(n,0)+1
    freq2={}
    for n3 in nums3:
        for n4 in nums4:
            n=n3+n4
            freq2[n]=freq2.get(n,0)+1
    for k,v in freq1.items():
        if -k in freq2:
            count+=freq1[k]*freq2[-k]
    return count
print(four_sum2(nums1, nums2, nums3, nums4))