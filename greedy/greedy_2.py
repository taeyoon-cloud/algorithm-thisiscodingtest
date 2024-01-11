n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

fir = arr[0]
sec = arr[1]

result = (fir * k + sec) * (m // (k+1)) + fir * (m % (k+1))

print(result)