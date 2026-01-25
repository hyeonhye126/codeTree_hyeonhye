arr = list(map(int, input().split()))

arr2 = []
for a in arr:
    if a != 0:
        arr2.append(a)
    if a == 0:
        break

print(sum(arr2), sum(arr2)/len(arr2))