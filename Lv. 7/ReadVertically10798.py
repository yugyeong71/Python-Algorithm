word = [[0] * 15 for i in range(5)]

for i in range(5):
    word_list = list(input())
    word_len = len(word_list)

    for j in range(word_len):
        word[i][j] = word_list[j]

for i in range(15):
    for j in range(5):
        if word[j][i] == 0:
            continue;
        else:
            print(word[j][i], end="")