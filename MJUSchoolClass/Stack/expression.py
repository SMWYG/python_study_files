"""
아래에 학번과 이름을 꼭 적으세요.

학번: 60131271
이름: 최다한
"""
from Stack import Stack


# 필요하면 추가로 함수를 만들어도 됩니다.

def __priority(token):
    if token == '*' or token == '/':
        return 2
    elif token == '+' or token == '-':
        return 1
    elif token == '(':
        return 0

def infix_to_postfix(str):
    stack = Stack()
    ret = []
    tokens = str.split()

    # 여기에 코드를 작성하시오.
    operator = ['*','/','+','-']
    openParentheses = '('
    closeParentheses = ')'
    for token in tokens:
        if token.isdigit():
            ret.append(token)
        elif token == openParentheses:
            stack.push(token)
        elif token == closeParentheses:
            while True:
                ret.append(stack.pop())
                if stack.peek() == openParentheses:
                    stack.pop()
                    break
        elif token in operator:
            if stack.is_empty() or __priority(token) > __priority(stack.peek()):
                stack.push(token)
            else:
                ret.append(stack.pop())
                stack.push(token)
    if not stack.is_empty():
        while not stack.is_empty():
            ret.append(stack.pop())
    return " ".join(ret)

def eval_postfix(str):
    stack = Stack()
    tokens = str.split()

    # 여기에 코드를 작성하시오.
    # 문자를 숫자로 바꾸는 방법 float("123") --> 123.0
    operator = ['*', '/', '+', '-']
    result = 0
    for token in tokens:
        if token.isdigit():
            stack.push(float(token))
        elif token in operator:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '*':
                stack.push(operand1*operand2)
            elif token == '/':
                stack.push(operand1/operand2)
            elif token == '+':
                stack.push(operand1+operand2)
            elif token == '-':
                stack.push(operand1-operand2)
    return stack.pop()

def expr_test(infix):
    postfix = infix_to_postfix(infix)
    result = eval_postfix(postfix)
    print("'%s' => '%s' = %f" % (infix, postfix, result))


if __name__ == '__main__':
    expr_test("4 + 3 - 2")
    expr_test("4 + 3 - 4 / 2")
    expr_test("1 + 2 * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 1 + 2 ) * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")

    # 실행 결과:
    # '4 + 3 - 2' = > '4 3 + 2 -' = 5.000000
    # '4 + 3 - 4 / 2' = > '4 3 + 4 2 / -' = 5.000000
    # '1 + 2 * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 3 * + 4 2 4 5 2 + - / * -' = 9.666667
    # '( 1 + 2 ) * 3 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 + 3 * 4 2 4 5 2 + - / * -' = 11.666667