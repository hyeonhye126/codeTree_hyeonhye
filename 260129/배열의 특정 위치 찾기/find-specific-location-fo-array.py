arr = list(map(int, input().split()))

even, three, cnt = 0, 0, 0

for i in range (len(arr)):
    if (i + 1) % 2 == 0:
        even += arr[i]
    if (i + 1) % 3 == 0:
        three += arr[i]
        cnt += 1

print(even, three / cnt)