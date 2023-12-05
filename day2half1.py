file = open("input.txt")

# 12 max red, 13 max green, 14 max blue

for line in file:
    line = line.strip()
    split = line.split(": ")[1]
    split = split.split(", ")
    for i in range(len(split)):
        if ";" in split[i]:
            try:
                split[i] = split[i].split("; ")[0]
                split = split.insert(i + 1, split[i].split("; ")[1])
            except IndexError:
                continue

    print(split)
