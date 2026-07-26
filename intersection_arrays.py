#Leetcode 349 Intersection of Two Arrays
nums1 = [1,2,2,1]
nums2 = [2,2]

def intersectionArrays(nums1,nums2):
    s1=set(nums1)
    s2=set(nums2)
    return list(s1.intersection(s2))
print(intersectionArrays(nums1,nums2))
