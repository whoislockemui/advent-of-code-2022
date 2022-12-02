input = open("input.txt", "r")

winningCombos = ["A Y", "B Z", "C X"]
itsATie = ["A X", "B Y", "C Z"]
score = 0

for line in input:
    if line.strip('\n') in winningCombos:
        score += 6
    elif line.strip('\n') in itsATie:
        score += 3
    
    if "X" in line:
        score += 1
    elif "Y" in line:
        score += 2
    else:
        score += 3

print(score)
