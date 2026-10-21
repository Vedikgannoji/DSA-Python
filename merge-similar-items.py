#2363 merge-similar-items
items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]

def merge_similar(items1,items2):
    overall={}
    items=items1+items2
    res = []
    for value,weight in items:
        overall[value]=overall.get(value,0)+weight
    for k,v in overall.items():
        res.append([k,v])
    res.sort()
    return res
print(merge_similar(items1,items2))
