#Leetcode 88 Merge Sorted Array Bruteforce

nums1 = [1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n=3

def merge(nums1,m,nums2,n):
    total=m+n
    j=0
    for i in range(m,total):
        nums1[i]=nums2[j]
        j+=1
    nums1.sort()
    return nums1
print(merge(nums1,m,nums2,n))