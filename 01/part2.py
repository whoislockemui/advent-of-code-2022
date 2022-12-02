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

calories.remove(maxCalories)
secondBest = max(calories)

calories.remove(secondBest)
thirdWorst = max(calories)

topCalories = maxCalories + secondBest + thirdWorst

print("Top 3 total:", topCalories)
