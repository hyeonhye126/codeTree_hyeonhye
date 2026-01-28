N = int(input())
arr = input().split()
even = []

for a in arr:
    if int(a) % 2 == 0:
        even.append(a)

print(' '.join(even[::-1]))