n, m = map(int, input().split())

result = 0

for _ in range(n):
    data = list(map(int, input().split()))
    result = max(min(data), result)

print(result)