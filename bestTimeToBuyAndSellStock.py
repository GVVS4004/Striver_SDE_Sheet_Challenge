from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    mxProfit=0
    mn=prices[0]
    start=0
    end=0
    while(start<len(prices) and end<len(prices)):
        start=end
        while(end<len(prices) and prices[end]<=mn):
            mn=prices[end]
            end+=1
        while(end<len(prices) and prices[end]>mn):
            mxProfit=max(prices[end]-mn,mxProfit)
            end+=1
    return mxProfit