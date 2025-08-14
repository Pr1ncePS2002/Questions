# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root) -> int:
        if root is None:
            return 0
        # return 1+ self.countNodes(root.left)+ self.countNodes(root.right)
        left_height=self.get_height(root.left)
        right_height=self.get_height(root.right)
        if left_height==right_height:
            total_left=2**left_height
            return total_left+self.countNodes(root.right)
        else:
            total_right=2**right_height
            return total_right+self.countNodes(root.left)

    def get_height(self,node):
        depth=0
        while node:
            depth+=1
            node=node.left
        return depth
        