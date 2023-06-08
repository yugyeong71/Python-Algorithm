N, K = map(int, input().split())

smallest = 0

for i in range(1, N + 1):
    if N % i == 0:
        K -= 1
        if K == 0:
            smallest = i
            break

print(smallest)
