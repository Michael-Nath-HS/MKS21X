from collections import deque


def converter(exp):
    '''
    :param exp:
    :return: str ans
    '''
    # creates a stack to use from the collections library
    stack = deque()
    # stores the output in a str ans
    ans = ""

    # dictionary holding precedence of operators
    priorities = {"+": ["+", "-", "*", "/"],
                  "-": ["+", "-", "*", "/"],
                  "*": ["*", "/"],
                  "/": ["*", "/"],
                  }
    # rules:
    # Read in the tokens one at a time
    # If a token is an integer, write it into the output
    # If a token is an operator, push it to the stack, if the stack is empty. If the stack is not empty, you pop entries with higher or equal priority and only then you push that token to the stack.
    # If a token is a left parentheses '(', push it to the stack
    # If a token is a right parentheses ')', you pop entries until you meet '('.
    # When you finish reading the string, you pop up all tokens which are left there.
    # Arithmetic precedence is in increasing order: '+', '-', '*', '/';
    exp = exp.split(" ")
    print(exp)
    for char in exp:
        if char in "()":
            if char == "(":
                stack.append(char)
            else:
                while "(" in stack:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        ans = ans + " " + stack.pop()
                    if len(stack) == 0:
                        break

        elif char in "+-*/":
            if len(stack) == 0:
                stack.append(char)
            else:
                while stack[-1] in priorities[char]:
                    ans = ans + " " + stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(char)

        try:
            int(char)
            ans = ans + " " + char
        except ValueError:
            continue

    while len(stack) != 0:
        ans = ans + " " + stack.pop()
    return ans


print(converter("21 + ( 4 + 3 * 2 + 1 ) / 3"))


