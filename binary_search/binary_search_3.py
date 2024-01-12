import sys

n, m = map(int, input().split())
cakes = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(array, start, end):
    maxim = 0
    while start <= end:
        h = (start + end) // 2

        total = 0
        for cake in array:
            if cake - h > 0:
                total += (cake - h)

        # 절단기 높이 높이기
        if total >= m:
            maxim = h
            start = h + 1
        # 절단기 높이 낮추기
        else:
            end = h - 1

    return maxim



max_cake = max(cakes)

print(binary_search(cakes, 1, max_cake))