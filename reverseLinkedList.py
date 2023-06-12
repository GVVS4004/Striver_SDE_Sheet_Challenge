from math import *
from collections import *
from sys import *
from os import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    # Write your code here.
    if head==None:
        return head
    ptr=None
    ptr1=head
    ptr2=head.next
    while(ptr2!=None):
        ptr1.next=ptr
        ptr=ptr1
        ptr1=ptr2
        ptr2=ptr2.next
    ptr1.next=ptr
    return ptr1



    pass
