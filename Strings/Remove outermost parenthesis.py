class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        x=0
        start=0
        for i,j in enumerate(s):
            if j=="(":
                if x==0:
                    start=i
                x+=1
            elif j==")":
                x-=1
                if x==0:
                    res.append(s[start+1:i])
                
        return "".join(res)
        