#Leetcode 1207 Unique Number of Occurrences
arr = [1,2,2,1,1,3]
def uniqueOccurances(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    
    occurances=set(freq.values())
    if len(occurances)!=len(freq):
        return False
    return True
print(uniqueOccurances(arr))