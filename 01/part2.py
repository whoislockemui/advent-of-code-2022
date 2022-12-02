input = open("input.txt", "r")

calories = []
total = 0

for line in input:
    if line != "\n":
        total += int(line)
    else:
        calories.append(total)
        total = 0

topCalories = 0

for n in range(3):
    topCalories += max(calories)
    calories.remove(max(calories))

print("Top 3 total:", topCalories)
