input = open("input.txt", "r")

maxCalories = 0
total = 0

for line in input:
    if line != "\n":
        total += int(line)
    else:
        if total > maxCalories:
            maxCalories = total
        total = 0

print("Elf with the most:", maxCalories)
