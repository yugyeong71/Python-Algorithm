s = int(input())

for i in range(s):
    r, p = input().split()
    for j in range(len(p)):
        print(p[j] * int(r), end= '')
    print('')