#118
numRows = 5
def pascalTriangle(numRows):
    if numRows==1:
        return [[1]]
    else:

        res=[]
        res.append([1])
        res.append([1,1])
        for i in range(2,numRows):
            res.append([1])
            for j in range(len(res[i-1])-1):
                res[i].append(res[i-1][j]+res[i-1][j+1])
            res[i].append(1)
    return res
print(pascalTriangle(numRows))

