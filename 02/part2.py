def shapePoints(input, outcome):
    if outcome == "win":
        if "A" in input:
            return 2
        elif "B" in input:
            return 3
        else:
            return 1
    elif outcome == "draw":
        if "A" in input:
            return 1
        elif "B" in input:
            return 2
        else:
            return 3
    else:
        if "A" in input:
            return 3
        elif "B" in input:
            return 1
        else:
            return 2

input = open("input.txt", "r")
score = 0

for line in input:
    if "X" in line:
        score += shapePoints(line, "lose")
    elif "Y" in line:
        score += 3
        score += shapePoints(line, "draw")
    else:
        score += 6
        score += shapePoints(line, "win")

print(score)
