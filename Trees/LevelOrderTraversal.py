# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root) :
        res=[]
        if not root:
            return []
        queue=deque([root])

        while queue:
            lvl=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                lvl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(lvl)
        return res