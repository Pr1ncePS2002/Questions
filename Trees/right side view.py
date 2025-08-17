# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root):
        # res=[]
        # def dfs(node,depth):
        #     if not node:
        #         return 
        #     if depth==len(res):
        #         res.append(node.val)
        #     dfs(node.right,depth+1)
        #     dfs(node.left,depth+1)
        # dfs(root,0)
        # return res
        
        if not root:
            return []
        res=[]
        stack=deque([root])
        while stack:
            size=len(stack)
            for i in range(size):
                node=stack.popleft()
                if i==size-1:
                    res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res

        