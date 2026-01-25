N = int(input())
score = list(map(float, input().split()))

avg = sum(score)/len(score)
print("%0.1f" %avg)

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")