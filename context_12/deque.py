# https://contest.yandex.ru/contest/23759/run-report/55335918/
class Deque:
    def __init__(self, queue_size):
        self.items = [None] * queue_size
        self.max_size = queue_size
        self.head = 0
        self.tail = -1
        self.size = 0

    def check_empty(self):
        if self.size == 0:
            raise IndexError('Исчерпание')

    def check_full(self):
        if self.size == self.max_size:
            raise IndexError('Переполнение')

    def push_front(self, value):
        self.check_full()
        head = (self.head - 1) % self.max_size
        self.items[head] = value
        self.head = head
        self.size += 1

    def push_back(self, value):
        self.check_full()
        tail = (self.tail + 1) % self.max_size
        self.items[tail] = value
        self.tail = tail
        self.size += 1

    def pop_front(self):
        self.check_empty()
        value = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def pop_back(self):
        self.check_empty()
        value = self.items[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value


if __name__ == '__main__':
    number_request = int(input())
    deque = Deque(int(input()))
    requests = [input().split(' ') for _ in range(number_request)]
    for command, *params in requests:
        try:
            result = getattr(deque, command)(*params)
            if not params:
                print(result)
        except IndexError:
            print('error')
        except AttributeError:
            raise ValueError(f'Неизвестная команда. {command}')
