# original function
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

# new function
def shapePointsTwo(input):
    if ("A X" in input) or ("B Z" in input) or ("C Y" in input):
        return 3
    elif ("A Z" in input) or ("B Y" in input) or ("C X" in input):
        return 2
    else:
        return 1

input = open("input.txt", "r")
score = 0

for line in input:
    if "X" in line: # lose
        score += shapePointsTwo(line)
    elif "Y" in line: # draw
        score += 3
        score += shapePointsTwo(line)
    else: # win
        score += 6
        score += shapePointsTwo(line)

print(score)
