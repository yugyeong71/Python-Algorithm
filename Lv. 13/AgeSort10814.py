N = int(input())

member = []

for _ in range(N):
    age, name = input().split()
    member.append((int(age), name))

member = sorted(member, key = lambda age: age[0])

for i in range(len(member)):
    print(*member[i])