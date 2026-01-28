n = int(input())

score = []
cnt = 0

for i in range (n):
    score.append(list(map(int, input().split())))

for i in range (n):
    if sum(score[i]) / 4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)