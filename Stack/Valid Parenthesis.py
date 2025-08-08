class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap= {')':'(',']':'[','}':'{'}

        for char in s:
            if char not in hashmap:        #if element not in the list append it
                stack.append(char)    
            else:
                if not stack:             #if stack is empty
                    return False
                else:
                    popped=stack.pop()      #else pop the element and check it with 
                    if popped!=hashmap[char]:
                        return False
        return not stack