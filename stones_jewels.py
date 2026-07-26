#Leetcode 771 Stones & Jewels Bruteforce
jewels = "aA"
stones = "aAAbbbb"

def jewels_stones(jewels,stones):
    res=0
    for stone in stones:
        if stone in jewels:
            res+=1
    return res
print(jewels_stones(jewels,stones))