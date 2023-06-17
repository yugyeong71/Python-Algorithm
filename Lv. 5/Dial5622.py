alphabet = input()

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

result = 0

for i in range(len(alphabet)):
    for j in dial:
        if alphabet[i] in j:
            result += dial.index(j) + 3

print(result)