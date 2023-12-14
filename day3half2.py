file = open("input.txt")

array = []
num = []
num_pos = []

numbers = "1234567890"

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
                                if array[coordinate[0] + i][coordinate[1] + j] == "*":
                                    gear_pos = (coordinate[0] + i, coordinate[1] + j)
                                    for k in range(-1, 2):
                                        for l in range(-1, 2):
                                            try:
                                                if array[gear_pos[0] + k][gear_pos[1] + l] in numbers:
                                                    new_num = [array[gear_pos[0] + k][gear_pos[1] + l]]
                                                    if array[gear_pos[0] + k][gear_pos[1] + l + 1] in numbers:
                                                        new_num.append(array[gear_pos[0] + k][gear_pos[1] + l + 1])
                                                        if array[gear_pos[0] + k][gear_pos[1] + l + 2] in numbers:
                                                            new_num.append(array[gear_pos[0] + k][gear_pos[1] + l + 2])
                                                    if array[gear_pos[0] + k][gear_pos[1] + l - 1] in numbers:
                                                        new_num.insert(0, array[gear_pos[0] + k][gear_pos[1] + l - 1])
                                                        if array[gear_pos[0] + k][gear_pos[1] + l - 2] in numbers:
                                                            new_num.insert(0,
                                                                           array[gear_pos[0] + k][gear_pos[1] + l - 2])
                                                print(new_num)
                                            except IndexError:
                                                continue
                            except IndexError:
                                continue
                num = []
                num_pos = []
                count = 0
            else:
                count = 0

print(num)
print(total)
