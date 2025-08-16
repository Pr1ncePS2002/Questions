class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
    
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ans=""
        for i in range(len(min(first,last))):
            if first[i]!=last[i]:
                return ans
            else:
                ans+=first[i]
        return ans
        