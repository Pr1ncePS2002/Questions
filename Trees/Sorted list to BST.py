# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findmiddle(start):
            prev=None
            slow=fast=start
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            if prev:
                prev.next=None
            return slow
        
        if not head:
            return None
        mid=findmiddle(head)
        root=TreeNode(mid.val)
        if head==mid:
            return root
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)

        return root
