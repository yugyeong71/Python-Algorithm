alphabet = input().upper()

alphabet_list = list(set(alphabet))

list = []

for i in alphabet_list:
    list.append(alphabet.count(i))

if list.count(max(list)) >= 2:
    print("?")

else:
    print(alphabet_list[(list.index(max(list)))])