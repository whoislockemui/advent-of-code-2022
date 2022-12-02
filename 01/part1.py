input = open("input.txt", "r")

calories = []
total = 0

for lines in input:
    if lines != "\n":
        total += int(lines)
    else:
        calories.append(total)
        total = 0

maxCalories = max(calories)

print("Elf with the most:", maxCalories)
