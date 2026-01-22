n = int(input())
score = ''

if n >= 90:
    score = 'A'
elif n >= 80:
    score = 'B'
elif n >= 70:
    score = 'C'
elif n >= 60:
    score = 'D'
else:
    score = 'F'

print(score)