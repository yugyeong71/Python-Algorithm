C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1 : ]) / N[0]
    cnt = 0
    for j in range(1, len(N)):
        if N[j] > avg:
            cnt += 1

    print('%.3f' % (cnt / N[0] * 100) + '%')