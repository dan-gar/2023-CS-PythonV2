from operator import add, mul, sub, truediv
from typing import List, Optional, Union


def prefix_evaluate(prefix_evaluation: List[str]) -> int:
    if prefix_evaluation=="":
        return None

    
    stack = []
    operators = set(['+', '-', '*', '/'])

    # reverse the list
    prefix_evaluation = prefix_evaluation[::-1]

    for i in prefix_evaluation:
        if i not in operators and i != ' ':
            stack.append(int(i))
        elif i != ' ':
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                res = a + b
            elif i == '-':
                res = a - b
            elif i == '*':
                res = a * b
            else:
                res = a / b  # division
            stack.append(res)

    return stack[0]

def to_prefix(equation: str) -> List[str]:
    if equation=="" or equation==None:
        return None
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

    lst=output[::-1]

    ret=''
    for i in lst:
        ret=ret+i+' '
    

    return ret[:-1]

def calculate(equation: str) -> int:
    return prefix_evaluate(to_prefix(equation))
