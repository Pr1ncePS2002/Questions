class Solution:
    def dailyTemperatures(self, temp) :
        n=len(temp)
        ans=[0]*n
        stack=[]
        for key,val in enumerate(temp):
            while stack and stack[-1][0]<val:
                stack_val,stack_key=stack.pop()
                ans[stack_key]=key-stack_key
            
            stack.append((val,key))

        return ans



        