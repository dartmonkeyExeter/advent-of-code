file = open("input.txt")

array = []
gear_one = []
gear_two = []

numbers = "1234567890"

total = 0

already_num = False

for line in file:
    array.append(list(line))

count = 0

for row_idx, row in enumerate(array):
    for cell_idx, cell in enumerate(row):
        if cell == "*":
            for i in (-1,2):
                for j in (-1,2):
                    if array[row_idx + i][cell_idx + j] in numbers:
                        if array[row_idx + i][cell_idx + j] in numbers:
                            gear_one = [array[row_idx + i][cell_idx + j]]
                            if array[row_idx + i][cell_idx + j] in numbers:
                                gear_one.insert(0, array[row_idx + i][cell_idx + j])
                                if array[row_idx + i][cell_idx + j] in numbers:
                                    gear_one.insert(0, array[row_idx + i][cell_idx + j])
                            if array[row_idx + i][cell_idx + j] in numbers:
                                gear_one.append(array[row_idx + i][cell_idx + j])
                                if array[row_idx + i][cell_idx + j] in numbers:
                                    gear_one.append(array[row_idx + i][cell_idx + j])


