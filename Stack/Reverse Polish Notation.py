from math import ceil,floor
class Solution:
    def evalRPN(self, tokens) -> int:
        stack=[]
        for i in tokens:
            if i in '+-*/':
                b,a=stack.pop(),stack.pop()

                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(a-b)
                elif i =='*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(i))
        return stack[0]

        