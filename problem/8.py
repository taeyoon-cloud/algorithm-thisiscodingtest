# 문자열 재정렬
s = input()

alphas = '' # 알파벳
total = 0 # 숫자의 합

for c in s:
    if c.isalpha():
        alphas += c
    elif c.isdigit():
        total += int(c)


result = "".join(sorted(alphas)) + str(total)

print(result)