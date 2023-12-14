file = open("input.txt")

array = []
num = []
num_pos = []

numbers = "1234567890\n"
numbers = list(numbers)

total = 0

already_num = False

for line in file:
    array.append(list(line))

count = 0

for row_idx, row in enumerate(array):
    for cell_idx, cell in enumerate(row):
        try:
            int(cell)
            count += 1
            if count != 0:
                num.append(cell)
                num_pos.append((row_idx, cell_idx))
        except ValueError:
            if count != 0:
                valid = False
                for coordinate in num_pos:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            try:
                                if (array[coordinate[0] + i][coordinate[1] + j] != "."
                                        and array[coordinate[0] + i][coordinate[1] + j] not in numbers):
                                    print(array[coordinate[0] + i][coordinate[1] + j])
                                    valid = True
                                    break
                            except IndexError:
                                continue
                        if valid:
                            break
                    if valid:
                        break
                if valid:
                    print("".join(num))
                    total += int("".join(num))
                num = []
                num_pos = []
                count = 0
            else:
                count = 0


print(num)
print(total)
