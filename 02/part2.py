def shapePointsTwo(input):
    if ("A X" in input) or ("B Z" in input) or ("C Y" in input): # use scissors
        return 3
    elif ("A Z" in input) or ("B Y" in input) or ("C X" in input): # use paper
        return 2
    else: # use rock
        return 1

input = open("input.txt", "r")
score = 0

for line in input:
    if "Z" in line: # win
        score += 6
    elif "Y" in line: # draw
        score += 3
    score += shapePointsTwo(line)

print(score)
