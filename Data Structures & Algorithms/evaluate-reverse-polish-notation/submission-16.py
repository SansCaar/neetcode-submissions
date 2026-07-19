class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = set(['+', '-', '*', '/'])
        l = []
        
        for i in range(len(tokens)):
            listLength = len(l)
            if tokens[i] not in operators:
                l.append(tokens[i])
            else:
                a = l.pop()
                b = l.pop()
                res = int(eval(f"{b} {tokens[i]} {a}"))
                l.append(res)
        return int(l.pop())