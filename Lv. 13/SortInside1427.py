num_list = list(map(int, str(input())))

num_list.sort(reverse=True)

for i in num_list:
    print(i, end='')