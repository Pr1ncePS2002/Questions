# Definition for singly linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    fast=head
    slow=head
    if head is None :
        return None
    
    while fast and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow