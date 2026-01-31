n = int(input())
arr = list(map(int, input().split()))

for i in range (0, n):
    min_idx = i
    for j in range (i, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for i in range (n):
    print(arr[i], end = ' ')


