# 18310번: 안테나
import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().rstrip().split()))
house.sort()

med = house[len(house)//2]


print(med)



