"""
아래에 학번과 이름을 꼭 적으세요.

학번: 60131271
이름: 최다한
"""
from stack import Stack

# 필요하면 추가로 함수를 만들어도 됩니다.


def infix_to_postfix(str):
    stack = Stack()
    ret = []
    tokens = str.split()

    # 여기에 코드를 작성하시오.
    open_ph = '('
    close_ph = ')'
    plus_minus = {'plus': {'flag': '+', 'prior': 1}, 'minus': {'flag': '-', 'prior': 1}}
    mul_div = {'mul': {'flag': '*', 'prior': 2}, 'div': {'flag': '/', 'prior': 2}}

    for token in tokens:
        if token.isdigit():
            ret.append(token)
        elif token == open_ph:
            stack.push(token)
        elif token == close_ph:
            while stack.peek() != open_ph:
                ret.append(stack.pop())
            stack.pop()
        elif token in [plus_minus['plus']['flag'], plus_minus['minus']['flag']]:
            if stack.peek() in [plus_minus['plus']['flag'], plus_minus['minus']['flag']]:
                ret.append(stack.pop())
                stack.push(token)
            else:
                stack.push(token)
        elif token in [mul_div['mul']['flag'], mul_div['div']['flag']]:
            if stack.peek() in [plus_minus['plus']['flag'], plus_minus['minus']['flag']]:
                ret.append(token)
            else:
                stack.push(token)

    while not stack.is_empty():
        ret.append(stack.pop())






    return " ".join(ret)


def eval_postfix(str):
    stack = Stack()
    tokens = str.split()

    # 여기에 코드를 작성하시오.
    # 문자를 숫자로 바꾸는 방법 float("123") --> 123.0
    return 999


def expr_test(infix):
    # postfix = infix_to_postfix(infix)
    # result = eval_postfix(postfix)
    # print("'%s' => '%s' = %f" % (infix, postfix, result))
    postfix = infix_to_postfix(infix)
    print("'%s' => '%s'" % (infix, postfix))

# 숫자는 여러 자리 숫자가 올 수도 있어요. 대신 연산자와 피 연산자는 공백문자로 나누어집니다.
if __name__ == '__main__':
    expr_test("14 + 3 - 2")
    expr_test("4 + 23 - 4 / 2")
    expr_test("1 + 2 * 43 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")
    expr_test("( 1 + 2 ) * 10 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )")

# 실행 결과:
# '14 + 3 - 2' = > '14 3 + 2 -' = 15.000000
# '4 + 23 - 4 / 2' = > '4 23 + 4 2 / -' = 25.000000
# '1 + 2 * 43 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 43 * + 4 2 4 5 2 + - / * -' = 89.666667
# '( 1 + 2 ) * 10 - 4 * ( 2 / ( 4 - ( 5 + 2 ) ) )' = > '1 2 + 10 * 4 2 4 5 2 + - / * -' = 32.666667
