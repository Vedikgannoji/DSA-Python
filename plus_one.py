#Leetcode 66 Plus one
digits = [1,2,3]
def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        