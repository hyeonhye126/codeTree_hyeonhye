N = int(input())

for i in range (N):
    cnt = 0
    for j in range(N, i, -1):
        for k in range(N, i, -1):
            cnt += 1
            if cnt != N - i:
                print("*", end = '')
            else:
                print("* ", end = '')
                cnt = 0
    print()