#1394 find-lucky-integer-in-an-array
arr = [2,2,3,4]
def lucky_integer(arr):
    freq={}
    res=[]
    for num in arr:
        freq[num]=freq.get(num,0)+1

    for k,v in freq.items():
        if k==v:
            res.append(k)
    if not res:
        return -1
    return max(res)
print(lucky_integer(arr))