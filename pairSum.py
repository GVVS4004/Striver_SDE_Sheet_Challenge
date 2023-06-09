from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    arr.sort()
    start=0
    end=len(arr)-1
    res=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==s:
                res.append([arr[i],arr[j]])
    return sorted(res,key= lambda x:x[0])
    pass