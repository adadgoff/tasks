# Дадыков Артемий - adadgoff@mail.ru
# https://contest.yandex.ru/contest/45468/problems/17/

from _collections import deque


def solve(_deq1: deque, _deq2: deque) -> str:

    moves = 0
    prizes = []

    while len(_deq1) != 0 and len(_deq2) != 0 and moves != 10 ** 6:
        first_deq1 = deq1.popleft()
        first_deq2 = deq2.popleft()

        prizes.append(first_deq1)
        prizes.append(first_deq2)

        if first_deq1 == first_deq2:
            moves += 1
            continue

        if first_deq1 == 0 and first_deq2 == 9:
            for prize in prizes:
                _deq1.append(prize)
            prizes = []
            moves += 1
            continue

        if first_deq1 == 9 and first_deq2 == 0:
            for prize in prizes:
                _deq2.append(prize)
            prizes = []
            moves += 1
            continue

        if first_deq1 > first_deq2:
            for prize in prizes:
                _deq1.append(prize)
            prizes = []
            moves += 1
            continue

        if first_deq1 < first_deq2:
            for prize in prizes:
                _deq2.append(prize)
            prizes = []
            moves += 1
            continue

    if len(_deq1) == 0:  # Второй игрок победил
        return f"second {moves}"

    elif len(_deq2) == 0:  # Первый игрок победил
        return f"first {moves}"

    else:  # Игра не завершилась за 10 ** 6 ходов
        return "botva"


if __name__ == "__main__":
    deq1 = deque([int(x) for x in input().split()])
    deq2 = deque([int(y) for y in input().split()])

    print(solve(deq1, deq2))
