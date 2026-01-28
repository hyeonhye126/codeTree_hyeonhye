num = list(map(int, input().split()))

result = 0
cnt = 0
for a in num:
    if a == 0:
        break
    if a % 2 == 0:
        cnt += 1
        result += a 

print(cnt, result)