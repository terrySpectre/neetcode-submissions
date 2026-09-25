class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        operators = {"+" : lambda a, b: a + b,
                     "-" : lambda a, b: a - b,
                     "*" : lambda a, b: a * b,
                     "/" : lambda a, b: int(a / b)}
        stack = []
        for i in tokens:
            if i in operators:
                int2 = stack.pop()
                int1 = stack.pop()
                stack.append(int(operators[i](int1, int2)))
            else:
                stack.append(int(i))
        return stack.pop()
        
                
