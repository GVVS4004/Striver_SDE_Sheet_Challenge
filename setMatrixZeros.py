from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    rows=set()
    cols=set()
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)
    for i in range(n):
        for j in range(m):
            if i in rows:
                matrix[i][j]=0
            if j in cols:
                matrix[i][j]=0
    # print(matrix)
    pass