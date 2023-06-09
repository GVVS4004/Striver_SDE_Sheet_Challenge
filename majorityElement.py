from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# Write your code here.
	di=dict(Counter(arr))
	for i in di:
		if di[i]>n//2:
			return i
	return -1
	pass