input = open("input.txt", "r")

calories = []
total = 0

for line in input:
    if line != "\n":
        total += int(line)
    else:
        calories.append(total)
        total = 0

maxCalories = max(calories)

print("Elf with the most:", maxCalories)
