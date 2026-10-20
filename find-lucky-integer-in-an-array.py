#1394 find-lucky-integer-in-an-array
arr = [2,2,3,4]
def lucky_integer(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1

    for k,v in freq.items():
        if k==v:
            return k
print(lucky_integer(arr))