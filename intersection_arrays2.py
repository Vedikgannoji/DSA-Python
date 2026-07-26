#Leetcode 350 Intersection of Two Arrays II
nums1 = [1,2,2,1]
nums2 = [2,2]

def intersectionArrays(nums1,nums2):
    freq={}
    res=[]
    for num in nums1:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for num in nums2:
        if num in freq and freq[num]>0:
            res.append(num)
            freq[num]-=1

    return res
print(intersectionArrays(nums1,nums2))
