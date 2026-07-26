# Leetcode 2032 Two Out of Three
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]

#using hashsets
def two_out_of_three(nums1,nums2,nums3):
    s1=set(nums1)
    s2=set(nums2)
    s3=set(nums3)

    return list((s1 & s2) | (s1 & s3) | (s2 & s3))
print(two_out_of_three(nums1,nums2,nums3))