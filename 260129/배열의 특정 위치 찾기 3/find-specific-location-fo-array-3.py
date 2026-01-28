arr = list(map(int, input().split()))

num = []
for a in arr:
    if a == 0:
        break
    num.append(a)

print(num[-3] + num[-2] + num[-1])