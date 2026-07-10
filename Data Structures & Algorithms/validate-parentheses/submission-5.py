class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for c in s:
            last = stack[len(stack) -1] if stack else ''

            if c in brackets and brackets[c] == last:
                stack.pop()
            else: 
                stack.append(c)

        print(len(stack))
        if stack:
            return False
        else:
            return True

                 

