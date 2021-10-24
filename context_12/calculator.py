# https://contest.yandex.ru/contest/23759/run-report/55254153/
import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('Стек пуст!')


def reversed_polish_notation(expressions,
                             stack=None, operators=OPERATORS,
                             digitizer=int):
    stack = Stack() if stack is None else stack
    for expression in expressions:
        if expression in operators:
            value_2, value_1 = stack.pop(), stack.pop()
            stack.push(operators[expression](value_1, value_2))
        else:
            try:
                stack.push(digitizer(expression))
            except ValueError:
                raise ValueError('Ошибка данных!'
                                 f'На вход пердано: {expression}')
    return stack.pop()


if __name__ == '__main__':
    try:
        print(reversed_polish_notation(input().split(' ')))
    except Exception as exception:
        print(exception)
