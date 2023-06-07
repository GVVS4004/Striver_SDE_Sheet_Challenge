# from os import *
# from sys import *
from collections import *
# from math import *

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    d=dict(Counter(arr))
    for i in d:
        if d[i]>=2:
            return int(i)
    pass