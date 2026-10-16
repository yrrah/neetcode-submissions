class Solution:
    def isValid(self, s: str) -> bool:
        closersByOpeners = {'(':')', '{':'}', '[':']'}

        stack = []

        for paren in s:
            if paren in closersByOpeners:
                stack.append(paren)
            else:
                if not stack:
                    return False
                if closersByOpeners[stack[-1]] != paren:
                    return False
                stack.pop()
        
        return not stack
        

        