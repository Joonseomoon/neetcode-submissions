class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        validOperators = ["+", "-", "*", "/"]
        for x in tokens:
            if x not in validOperators:
                operandStack.append(int(x))
            else:
                if x == "+":
                    op1 = operandStack.pop()
                    op2 = operandStack.pop()
                    subVal = op1 + op2
                    operandStack.append(subVal)
                if x == "-":
                    op1 = operandStack.pop()
                    op2 = operandStack.pop()
                    subVal = op2 - op1
                    operandStack.append(subVal)
                if x == "*":
                    op1 = operandStack.pop()
                    op2 = operandStack.pop()
                    subVal = op1 * op2
                    operandStack.append(subVal)
                if x == "/":
                    op1 = operandStack.pop()
                    op2 = operandStack.pop()
                    subVal = int(op1 / op2)
                    operandStack.append(subVal)
        return operandStack[0]