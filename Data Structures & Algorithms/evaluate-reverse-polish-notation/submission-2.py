class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                int2, int1 = stack.pop(), stack.pop()
                stack.append(int1 + int2)
            elif i == "-":
                int2, int1 = stack.pop(), stack.pop()
                stack.append(int1 - int2)
            elif i == "*":
                int2, int1 = stack.pop(), stack.pop()
                stack.append(int1 * int2)
            elif i == "/":
                int2, int1 = stack.pop(), stack.pop()
                stack.append(int(int1 / int2))
            else:
                stack.append(int(i))
        return stack.pop()
        
                
