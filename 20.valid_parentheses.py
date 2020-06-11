# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        couples = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        
        for c in s:
            if c in couples.keys():
                top_elem = stack.pop() if stack else None
                if top_elem != couples[c]:
                    return False
            else:   
                stack.append(c)

        if len(stack):
            return False
    
        return True