file = open("input.txt")

# 12 max red, 13 max green, 14 max blue

colour_to_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

colour_to_min = {
    "red": 0,
    "green": 1,
    "blue": 2,
}

minimums = [0, 0, 0]

answer = 0

for line in file:
    minimums = [0, 0, 0]
    line = line.strip()

    games = line.split(": ")[1]
    games = games.replace(";", ",")
    games = games.split(", ")

    for i in games:
        amount = int(i.split(" ")[0])
        colour = i.split(" ")[1].strip()
        maximum = colour_to_max[colour]
        minimum = colour_to_min[colour]

        if minimums[minimum] < amount:
            minimums[minimum] = amount
    print(minimums)

    answer += minimums[0] * minimums[1] * minimums[2]

print(answer)
