# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder,inorder):
        index={}
        for idx in range(len(inorder)):
            index[inorder[idx]]=idx
        self.pre_index=0
        def helper(l,r):
            if l>r:
                return None

            root_val=preorder[self.pre_index]
            self.pre_index+=1
            root=TreeNode(root_val)

            root.left=helper(l,index[root_val]-1)
            root.right=helper(index[root_val]+1,r)

            return root
        return helper(0,len(inorder)-1)