# 1715번: 카드 정렬하기
import sys
import heapq # 힙 사용
input = sys.stdin.readline

n = int(input())
card = []

for _ in range(n):
    heapq.heappush(card, int(input()))

total = 0
for i in range(n-1):
    fir = heapq.heappop(card)
    sec = heapq.heappop(card)

    temp = fir + sec
    total += temp
    
    heapq.heappush(card, temp)

print(total)
    




