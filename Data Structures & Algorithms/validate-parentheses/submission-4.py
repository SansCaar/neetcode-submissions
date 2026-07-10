class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for c in s:
            if c not in brackets:
                print(c)
                stack.append(c)
            else: 
                last = stack[len(stack) -1] if stack else ''
                if brackets[c] == last:
                    stack.pop()
                else: 
                    stack.append(c)

        print(len(stack))
        if stack:
            return False
        else:
            return True

                 

