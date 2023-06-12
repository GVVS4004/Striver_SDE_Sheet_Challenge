from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    d=set()
    for i in arr:
        d.add(i)
    mx=1
    for i in range(len(arr)):
        if arr[i]-1 not in d:
            x=arr[i]
            count=1
            while(True):
                if x+1 in d:
                    x+=1
                    count+=1
                    mx=max(mx,count)
                else:
                    break
    return mx
                
    pass
