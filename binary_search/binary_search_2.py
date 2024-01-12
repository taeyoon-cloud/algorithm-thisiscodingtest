n = int(input())
stock = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))


def binary_search(array, target, start ,end):
    if start > end:
        return "no"
    
    mid = (start + end) // 2

    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


stock.sort() # 이거 까먹으면 안됨

for c in check:
    print(binary_search(stock, c, 0, len(stock)-1), end=' ')