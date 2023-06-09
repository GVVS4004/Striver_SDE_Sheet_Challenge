def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    col=len(mat[0])
    row=len(mat)
    # i=0
    # j=col
    # while(j>=0 and i<=row):
    #     if mat[i][j]==target:
    #         return True
    #     elif mat[i][j]>target:
    #         j-=1
    #     else:
    #         i+=1
    # return False
    low=0
    high=(row*col)-1
    while(low<=high):
        mid=(low+high)//2
        if mat[mid//col][mid%col]==target:
            return True
        if mat[mid//col][mid%col]<target:
            low=mid+1
        else:
            high=mid-1
    return  False 
    
    pass
