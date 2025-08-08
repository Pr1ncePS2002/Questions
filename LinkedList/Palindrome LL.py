# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if head is None or head.next is None:         # vals=[]
            return True                               # while head:
        fast=slow=head                                       # vals.append(head.val)
        while fast and fast.next:                            #head=head.next
            slow=slow.next                             #return vals==vals[::-1]
            fast=fast.next.next
        prev=None
        cur=slow
        while cur:
            nextnode=cur.next
            cur.next=prev
            prev=cur
            cur=nextnode
        first =head
        second=prev
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
                                                                
                                                               
                                                               
                                                                
                                                                

        