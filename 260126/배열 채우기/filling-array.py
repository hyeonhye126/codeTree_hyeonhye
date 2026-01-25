arr = list(map(int, input().split()))

if arr[-1] == 0:
    arr.pop(-1)

reversed_arr = arr[::-1]
for a in reversed_arr:
    print(a, end = ' ')