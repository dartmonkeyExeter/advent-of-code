file_input = open("input.txt")
total = 0

for line in file_input:
    int_list = []

    for char_idx, char in enumerate(line):
        try:
            int_list.append(int(char))
        except ValueError:
            continue

    first_value = int_list[0]
    second_value = int_list[-1]

    print(f'{first_value}{second_value}')
    total += int(f'{first_value}{second_value}')


print(total)
