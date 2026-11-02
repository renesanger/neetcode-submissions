class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() 
                    #if stack is empty and 
                    #top of the stack is its open parenthesis
                    #pop it from the stack otherwise its invalid 
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False