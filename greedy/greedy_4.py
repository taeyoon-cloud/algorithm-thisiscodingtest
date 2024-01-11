n, k = map(int, input().split())

count = 0
while True:
    if n % k == 0:
        n //= k
        count += 1
    if n < k:
        break
    else:
        count += n%k
        n -= (n%k)
        

    print(n, count)

print(count + (n%k) - 1)