level = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

grade = 0
total = 0

for i in range(20):
    A, B, C = map(str, input().split())
    if C == level[9]:
        continue
    grade += float(B)
    D = level.index(C)
    total += float(B) * (score[D])

print("%f" % (total / grade))