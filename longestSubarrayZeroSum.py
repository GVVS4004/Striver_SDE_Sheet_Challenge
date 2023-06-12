from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    # mx=0
    # for i in range(len(arr)):
    #     count=0
    #     for j in range(i,len(arr)):
    #         count+=arr[j]
    #         if count==0:
    #             mx=max(mx,j-i+1)
    mx=0
    preSum={}

    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==0:
            mx=max(mx,i+1)
        if sum in preSum:
            ind=preSum[sum]
            mx=max(mx,i-ind)
        if sum not in preSum:
            preSum[sum]=i
    return mx

    pass