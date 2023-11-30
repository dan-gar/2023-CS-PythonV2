from operator import add, mul, sub, truediv
from typing import List, Optional, Union


def prefix_evaluate(prefix_evaluation: List[str]) -> int:
    stack = []
    operators = set(['+', '-', '*', '/'])

    for i in reversed(range(len(prefix_evaluation))):
        if prefix_evaluation[i] in operators:
            a = stack.pop()
            b = stack.pop()
            if prefix_evaluation[i] == '+':
                stack.append(a + b)
            elif prefix_evaluation[i] == '-':
                stack.append(a - b)
            elif prefix_evaluation[i] == '*':
                stack.append(a * b)
            elif prefix_evaluation[i] == '/':
                stack.append(int(a / b))
        elif prefix_evaluation[i].strip():  # Skip spaces
            stack.append(int(prefix_evaluation[i]))

    return stack[0]


def to_prefix(equation: str) -> List[str]:
    stack = []
    output = []
    operators = set(['+', '-', '*', '/', '(', ')'])
    precedence = {'+':1, '-':1, '*':2, '/':2}

    equation = equation.replace(" ", "")
    equation = list(equation)[::-1]

    for char in equation:
        if char not in operators:
            output.append(char)
        elif char==')':
            stack.append(')')
        elif char=='(':
            while stack and stack[-1]!=')':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1]!=')' and precedence[char]<=precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return output[::-1]

def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
