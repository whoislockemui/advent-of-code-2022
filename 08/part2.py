def sceneValue(value, comparisonString):
    score = 0
    for eachThing in comparisonString:
        score += 1
        if int(value) <= int(eachThing):
            return score
    return score

input = open("input.txt", "r")

trees = []

for line in input:
    trees.append(line.rstrip())

row = 0
column = 0
bestScore = 0

while row < len(trees): # we still have rows
    while column < len(trees[0]): # for each item
        left = trees[row][:column]
        leftSide = left[::-1] # needs to be listed from closest tree to farthest
        rightSide = trees[row][column+1:len(trees[row])]

        topSide = ""
        bottomSide = ""

        for n in range(0, row):
            topSide = trees[n][column] + topSide # needs to be listed from closest tree to farthest

        for n in range(row+1, len(trees)):
            bottomSide = bottomSide + trees[n][column]

        leftScore = sceneValue(trees[row][column], leftSide)
        rightScore = sceneValue(trees[row][column], rightSide)
        topScore = sceneValue(trees[row][column], topSide)
        bottomScore = sceneValue(trees[row][column], bottomSide)

        treeScore = leftScore * rightScore * topScore * bottomScore

        if treeScore > bestScore:
            bestScore = treeScore

        column += 1
    row += 1
    column = 0 # reset column counter

print("highest score:", bestScore)
