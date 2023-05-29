# Дадыков Артемий - adagoff@mail.ru
# https://contest.yandex.ru/contest/45468/problems/11/

class Stack:
    def __init__(self):
        self._size = 0
        self._capacity = 10
        self._array = [None] * self._capacity

    def push(self, value):
        if self._size == self._capacity:
            self._array = self._array + [None] * self._capacity
            self._capacity *= 2

        self._array[self._size] = value
        self._size += 1
        return "ok"

    def pop(self):
        if self._size == 0:
            return "error"
        self._size -= 1
        temporary = self._array[self._size]
        self._array[self._size] = None
        return temporary

    def back(self):
        if self._size == 0:
            return "error"
        return self._array[self._size - 1]

    def size(self):
        return self._size

    def clear(self):
        self._size = 0
        self._capacity = 10
        self._array = [None] * self._capacity
        return "ok"


if __name__ == "__main__":

    stack = Stack()

    while (cmd := input().split())[0] != "exit":
        if cmd[0] == "push":
            print(stack.push(int(cmd[1])))

        elif cmd[0] == "pop":
            print(stack.pop())

        elif cmd[0] == "back":
            print(stack.back())

        elif cmd[0] == "size":
            print(stack.size())

        elif cmd[0] == "clear":
            print(stack.clear())

    print("bye")
