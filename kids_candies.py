#Leetcode 1431  Kids With the Greatest Number of Candies
candies = [2,3,5,1,3]
extraCandies = 3
def kidsCandies(candies,extraCandies):
    res=[]
    greatest=max(candies)
    for candy in candies:
        res.append(candy + extraCandies >= greatest)
    return res
print(kidsCandies(candies,extraCandies))

