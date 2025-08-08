class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=left=0
        count={}
        for right,c in enumerate(s):
            if c in count:
                count[c]+=1
            else:                   #push each value count to dictionary
                count[c]=1
            while count[c]>1:            
                count[s[left]]-=1    #remove the count of value at 0 index and move the pointer 
                left+=1                 #now the pointer points to 2nd element, if its count is greater than 1 
            max_len=max(max_len,right-left+1)
        return max_len