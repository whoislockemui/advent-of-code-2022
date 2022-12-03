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
def shapePointsTwo(input,outcome):
    if ("A" in input and outcome == "lose") or ("B" in input and outcome == "win") or ("C" in input and outcome == "draw"):
        return 3
    elif ("A" in input and outcome == "win") or ("B" in input and outcome == "draw") or ("C" in input and outcome == "lose"):
        return 2
    else:
        return 1

input = open("input.txt", "r")
score = 0

for line in input:
    if "X" in line:
        score += shapePointsTwo(line, "lose")
    elif "Y" in line:
        score += 3
        score += shapePointsTwo(line, "draw")
    else:
        score += 6
        score += shapePointsTwo(line, "win")

print(score)
