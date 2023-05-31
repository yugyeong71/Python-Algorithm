N = int(input())

colored_paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            colored_paper[i][j] = 1

answer = 0

for row in colored_paper:
    answer += row.count(1)

print(answer)