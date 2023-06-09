from math import *
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	# Write your code here.
	di=dict(Counter(arr))
	n=len(arr)
	res=[]
	for i in di:
		if di[i]>(n//3):
			res.append(i)
	return res
	pass