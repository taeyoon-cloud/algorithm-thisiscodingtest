# 10825번: 국영수
import sys
input = sys.stdin.readline

n = int(input())
student = [] # (학생이름, 국어점수, 영어점수, 수학점수)


for _ in range(n):
    name, a, b, c = input().rstrip().split()
    student.append((name, int(a), int(b), int(c)))


student.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for s in student:
    print(s[0])