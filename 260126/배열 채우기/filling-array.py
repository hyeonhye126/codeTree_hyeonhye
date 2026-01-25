arr = input().split()

if arr[-1] == '0':
    arr.pop(-1)

print(' '.join(arr[::-1]))