#Leetcode 771 Stones & Jewels Hashmap
jewels = "aA"
stones = "aAAbbbb"

def jewels_stones(jewels,stones):
    jewel_set=set(jewels)
    res=0
    for stone in stones:
        if stone in jewel_set:
            res+=1
    return res
print(jewels_stones(jewels,stones))
