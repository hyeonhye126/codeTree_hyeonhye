arr = list(map(int, input().split()))

sum_ = 0
cnt = 0

for a in arr:
    if a < 250:
        sum_ += a
        cnt += 1
    if a >= 250:
        break

avg = sum_ / cnt

print("%d %.1f" %(sum_, avg))
