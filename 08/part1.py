def checkVisible(value, comparisonString):
    for eachThing in comparisonString:
        if int(value) <= int(eachThing):
            return False
    return True # it is never smaller than anything else

input = open("input.txt", "r")

trees = []

for line in input:
    trees.append(line.rstrip())

visible = 0
row = 0
column = 0

while row < len(trees): # we still have rows
    while column < len(trees[0]): # for each item
        leftSide = trees[row][:column]
        rightSide = trees[row][column+1:len(trees[row])]

        topSide = ""
        bottomSide = ""

        for n in range(0, row):
            topSide = topSide + trees[n][column]

        for n in range(row+1, len(trees)):
            bottomSide = bottomSide + trees[n][column]

        if checkVisible(trees[row][column], leftSide) or checkVisible(trees[row][column], rightSide) \
            or checkVisible(trees[row][column], topSide) or checkVisible(trees[row][column], bottomSide):
            visible += 1

        column += 1
    row += 1
    column = 0 # reset column counter

print("visible trees:", visible)
