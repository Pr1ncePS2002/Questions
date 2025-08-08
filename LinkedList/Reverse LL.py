# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev        
        # if head is None or head.next is None:
        #     return head
        # small_ll=self.reverseList(head.next)
        # finaltail=head.next
        # finaltail.next=head
        # head.next=None

        # return small_ll

