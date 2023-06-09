from math import *
from collections import *
from sys import *
from os import *

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
	# Write your code here.
	res=1
	a=x
	while(n>0):
		if (n%2!=0):
			res=((res)%m*(a)%m)%m
		a=((a)%m*(a)%m)%m
		n=n>>1
	return res%m
	pass

# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1