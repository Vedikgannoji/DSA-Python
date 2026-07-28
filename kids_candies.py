#Leetcode 1431  Kids With the Greatest Number of Candies
candies = [2,3,5,1,3]
extraCandies = 3
def kidsCandies(candies,extraCandies):
    res=[]
    greatest=max(candies)
    for candy in candies:
        if candy+extraCandies>=greatest:
            res.append("True")
        else:
            res.append("False")
    return res
print(kidsCandies(candies,extraCandies))

