from typing import dataclass_transform
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Solution:
    def reverse_DLL(self,head):
        if head is None or head.next is None:
            return head
        curr=head
        newhead=None
        while curr is not None:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp 
            
            newhead=curr
            curr=curr.prev
        return newhead       