from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
	# Write your code here.
    def merge(arr,l,r,mid,count):
        i=l
        j=mid+1
        for i in range(l, mid+1):
            while j<=r and arr[i]>arr[j]:
                j += 1
            count[0] += (j-(mid+1))

        i=l
        j=mid+1
        temp=[]
        while(i<=mid and j<=r):
            if arr[i]<arr[j]:
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
    mergeSort(arr,0,n-1,count)
    # print(arr)
    return count[0]

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))