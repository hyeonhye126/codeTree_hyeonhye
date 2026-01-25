arr = list(map(int, input().split()))

arr2 = []
for a in arr:
    if a != 0:
        arr2.append(a)

reversed_arr = arr2[::-1]
for a in reversed_arr:
    print(a, end = ' ')