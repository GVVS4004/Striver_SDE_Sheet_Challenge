from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here
    se=set()
    sm=0
    for i in range(n):
        if arr[i] in se:
            x=arr[i]
        se.add(arr[i])
        sm+=arr[i]
    summation=(n*(n+1))//2
    return summation-sm+x,x
    pass
