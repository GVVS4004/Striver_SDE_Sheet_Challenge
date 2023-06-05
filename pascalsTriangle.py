# from os import *
# from sys import *
# from collections import *
# from math import *

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    res=[[1]]
    if n==1:
        return res
    for i in range(1,n):
        res.append([1]*(i+1))
        for j in range(1,len(res[i-1])):
            # temp.append(res[i-1][j-1]+res[i-1][j])
            res[i][j]=res[i-1][j-1]+res[i-1][j]
        # temp.append(1)
        # res.append(temp)
    # print(res)
    return res
    pass