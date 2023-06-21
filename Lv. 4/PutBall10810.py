N, M = map(int, input().split())

ball_list = [0] * N

for i in range(M):
  a, b, c = map(int,input().split())
  for j in range(a, b + 1):
    ball_list[j - 1] = c

for j in range(N):
  print(ball_list[j], end=" ")