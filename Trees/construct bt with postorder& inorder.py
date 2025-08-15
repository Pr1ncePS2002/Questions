# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # Create index_map using a normal for loop
        index_map = {}
        for idx in range(len(inorder)):
            index_map[inorder[idx]] = idx
        
        self.post_idx = len(postorder) - 1  # Start from last element

        def helper(left, right):
            if left > right:
                return None
            
            # Pick current root from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            # Build right subtree first
            root.right = helper(index_map[root_val] + 1, right)
            root.left = helper(left, index_map[root_val] - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)