from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

    # Your code here
    # return the answer
    start=0
    end=0
    mxSum=0
    while(start<n and end<n):
        start=end
        sm=0
        while(sm>=0 and end<n):
            sm+=arr[end]
            end+=1
            mxSum=max(sm,mxSum)
    return mxSum































#taking inpit using fast I/O
def takeInput() :
    
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
