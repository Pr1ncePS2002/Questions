class Solution:
    def maxDepth(self, s: str) -> int:
        cur_depth=0
        max_depth=0
        for i in s:
            if i =='(':
                cur_depth+=1
                max_depth=max(cur_depth,max_depth)
            elif i==')':
                cur_depth-=1
        return max_depth
        