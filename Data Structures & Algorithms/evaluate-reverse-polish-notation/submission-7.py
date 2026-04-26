class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        for x in tokens:
            if x not in "+-*/":
                operandStack.append(int(x))
            else:
                op1 = operandStack.pop()
                op2 = operandStack.pop()
                if x == "+":
                    operandStack.append(op1 + op2)
                if x == "-":
                    operandStack.append(op2 - op1)
                if x == "*":
                    operandStack.append(op1 * op2)
                if x == "/":
                    operandStack.append(int(float(op2) / op1))
        return operandStack[0]