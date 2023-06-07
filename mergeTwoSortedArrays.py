from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    ptr1=m-1
    ptr2=n-1
    ptr=len(arr1)-1
    while(ptr1>=0 and ptr>=0 and ptr2>=0):
        # print("arr1",arr1)
        if arr1[ptr1]>arr2[ptr2]:
            arr1[ptr]=arr1[ptr1]
            arr1[ptr1]=0
            ptr1-=1
            ptr-=1
        else:
            arr1[ptr]=arr2[ptr2]
            ptr2-=1
            ptr-=1
    while(ptr2!=-1):
        arr1[ptr]=arr2[ptr2]
        ptr2-=1
        ptr-=1
   
    return arr1
    

    pass
