#2053 kth-distinct-string-in-an-array
arr = ["d","b","c","b","c","a"]
k = 2
def kth_distinct_string_array(arr,k):
    freq={}
    res=[]
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for num in arr:
        if freq[num]==1:
            res.append(num)
    return res[k-1]
print(kth_distinct_string_array(arr,k))