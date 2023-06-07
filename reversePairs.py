from os import *
from sys import *
from collections import *
from math import *

def reversePairs(arr, n):
    # Write your code here.
    def merge(arr,l,r,mid,count):
            # i=l
            j=mid+1
            temp=[]
            for i in range(l, mid+1):
                while j<=r and arr[i]>2*arr[j]:
                    j += 1
                count[0] += (j-(mid+1))
            i=l
            j=mid+1
            while(i<=mid and j<=r):
                # print(arr[i],arr[j])
                if arr[i]<=arr[j]:
                    temp.append(arr[i])
                    i+=1
                else:
                    temp.append(arr[j])
                    j+=1
                    
            while(i<=mid):
                temp.append(arr[i])
                i+=1
            while(j<=r):
                temp.append(arr[j])
                j+=1
            # print("temp",temp)
            for i in range(l,r+1):
                arr[i]=temp[i-l]
    def mergeSort(arr,l,r,count):
        if l==r:
            return
        mid=(l+r)//2
        mergeSort(arr,l,mid,count)
        mergeSort(arr,mid+1,r,count)
        merge(arr,l,r,mid,count)


    count=[0]
    mergeSort(arr,0,len(arr)-1,count)
    return count[0]
    
    pass