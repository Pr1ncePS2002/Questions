# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def height(node):
            if not node:
                return 0
            leftheight=height(node.left)
            if leftheight==-1:
                return -1
            
            rightheight=height(node.right)
            if rightheight==-1:
                return -1

            if abs(leftheight-rightheight)>1:
                return -1
            ans_height=1+max(leftheight,rightheight)
            return ans_height

        return height(root)!= -1