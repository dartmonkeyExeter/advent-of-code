from copy import deepcopy

file = open("input.txt")

# 12 max red, 13 max green, 14 max blue

colour_to_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
answer = 0

for line in file:

    line = line.strip()

    ID = line.strip("Game ")
    ID = ID.strip()
    ID = int(ID.split(": ")[0])
    games = line.split(": ")[1]
    games = games.split(", ")

    new_games = []

    for i in games:
        if ";" in i:
            formatted = i.split("; ")
            new_games.append(formatted[0])
            new_games.append(formatted[1])
        else:
            new_games.append(i)

    impossible = 0
    for i in new_games:
        amount = int(i.split(" ")[0])
        colour = i.split(" ")[1]
        maximum = colour_to_max[colour]
        if amount > maximum:
            impossible = 1
            break
    if impossible == 0:
        answer += ID

print(answer)
