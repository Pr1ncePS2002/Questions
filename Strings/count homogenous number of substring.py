class Solution:
    def countHomogenous(self, s: str) -> int:
        count=0
        streak=0
        for i in range(len(s)):
            if i>0 and s[i]==s[i-1]:
                streak+=1
            else:
                streak=1
            count=(count+streak)%1000000007
        return count
        