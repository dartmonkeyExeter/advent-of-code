file_input = open("input.txt")
total = 0

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
words_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in file_input:
    int_list = []
    int_idx_list = []

    str_list = []
    str_idx_list = []

    for char_idx, char in enumerate(line):
        try:
            int_list.append(int(char))
            int_idx_list.append(char_idx)
        except ValueError:
            continue

    yippie = False

    for char_idx, char in enumerate(line):
        for word in words:
            for letter_idx, letter in enumerate(word):
                yippie = True
                if letter != line[char_idx + letter_idx]:
                    yippie = False
                    break
            if yippie:
                str_list.append(words_to_num[word])
                str_idx_list.append(char_idx)

    try:
        if str_idx_list[0] < int_idx_list[0]:
            first_value = str_list[0]
        else:
            first_value = int_list[0]
    except IndexError:
        first_value = int_list[0]

    try:
        if str_idx_list[-1] > int_idx_list[-1]:
            second_value = str_list[-1]
        else:
            second_value = int_list[-1]
    except IndexError:
        second_value = int_list[-1]

    print(f'{first_value}{second_value}')
    total += int(f'{first_value}{second_value}')


print(total)
