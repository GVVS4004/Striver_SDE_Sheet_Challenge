'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def removeKthNode(head, k):
    # Write your code here.
    slow=head
    fast=head
    count=0
    x=k
    while(fast!=None):
        if k==-1:
            fast=fast.next
            slow=slow.next
        else:
            fast=fast.next
            k-=1
        count+=1
    
    if count==x:
        return head.next
    slow.next=slow.next.next
    return head
    pass