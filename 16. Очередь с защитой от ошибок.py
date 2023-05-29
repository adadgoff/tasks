# Дадыков Артемий - adagoff@mail.ru
# https://contest.yandex.ru/contest/45468/problems/16/

class Dequeue:

    def __init__(self):
        self._size = 0
        self._capacity = 10
        self._array = [None] * self._capacity
        self._head = self._capacity // 3
        self._tail = self._capacity // 3

    def __str__(self):
        dequeue_elements = [self._array[(self._head + index) % self._capacity] for index in range(self._size)]
        return '[' + ', '.join([str(x) for x in dequeue_elements]) + ']'

    def __len__(self):
        return self._size

    def front(self):
        return self._array[self._head]

    def back(self):
        return self._array[self._tail - 1]

    def pop_front(self):  # Удаление с начала
        temporary = self._array[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return temporary

    def pop_back(self):  # Удаление с конца
        temporary = self.back()
        self._tail = (self._tail - 1) % self._capacity
        self._size -= 1
        return temporary

    # Как же круто, что в python'е реализован остаток деления по математически,
    # а то в плюсах пришлось реализовывать это, хотя вроде и не такая сложная это и задача :)
    def push_front(self, value):  # Добавление в начало
        if self._size == self._capacity:
            self._array = [None] * (self._capacity // 2) + self._array[self._head:] + self._array[:self._head] + [None] * (self._capacity // 2)
            self._head = self._capacity // 2
            self._tail = self._capacity + self._capacity // 2
            self._capacity = self._capacity * 2
        self._head = (self._head - 1) % self._capacity
        self._array[self._head] = value
        self._size += 1

    def push_back(self, value):  # Добавление в конец
        if self._size == self._capacity:
            self._array = [None] * (self._capacity // 2) + self._array[self._head:] + self._array[:self._head] + [None] * (self._capacity // 2)
            self._head = self._capacity // 2
            self._tail = self._capacity + self._capacity // 2
            self._capacity = self._capacity * 2
        self._array[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1

    def size(self):
        return self._size

    def __iter__(self):
        for index in range(self._size):
            yield self._array[(self._head + index) % self._capacity]

    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._array[(self._head + index) % self._capacity]
        raise Exception("Index out of range")


if __name__ == "__main__":
    deque = Dequeue()
    while (cmd := input().split())[0] != "exit":
        if cmd[0] == "push":
            deque.push_back(int(cmd[1]))
            print("ok")

        elif cmd[0] == "pop":
            if deque.size() > 0:
                print(deque.pop_front())
            else:
                print("error")

        elif cmd[0] == "front":
            if deque.size() > 0:
                print(deque.front())
            else:
                print("error")

        elif cmd[0] == "size":
            print(deque.size())

        elif cmd[0] == "clear":
            deque = Dequeue()
            print("ok")

    print("bye")