input = open("input.txt", "r")

# separate out the supply arrangement lines of input
n = 0
supplyArrangement = [input.readline()]
actions = []

while supplyArrangement[n].startswith(" 1") is False:
    supplyArrangement.append(input.readline())
    n += 1

# grab the last line of the supply arrangement to know how many stacks
stacksOnly = supplyArrangement.pop()
numStacks = stacksOnly[len(stacksOnly)-3]

stack = []
i = 0

# each item in the stack list is a stack
while i < int(numStacks):
    stack.append("")
    i += 1

for row in supplyArrangement:
    stack[0] = row[1] + stack[0].rstrip()
    stack[1] = row[5] + stack[1].rstrip()
    stack[2] = row[9] + stack[2].rstrip()
    stack[3] = row[13] + stack[3].rstrip()
    stack[4] = row[17] + stack[4].rstrip()
    stack[5] = row[21] + stack[5].rstrip()
    stack[6] = row[25] + stack[6].rstrip()
    stack[7] = row[29] + stack[7].rstrip()
    stack[8] = row[33] + stack[8].rstrip()

# the rest of the input lines are actions
for line in input:
    actions.append(line.strip())

actions.pop(0) # dump blank line

startingStackNumber = []
targetStackNumber = []
numberToMove = []

for each in actions:
    slices = each.split()
    numberToMove.append(slices[1])
    startingStackNumber.append(slices[3])
    targetStackNumber.append(slices[5])

j = 0
print(len(numberToMove))
while j < len(numberToMove):
    originalStack = stack[int(startingStackNumber[j])-1]
    print("loop", j)
    print(originalStack, originalStack[:-int(numberToMove[j])], originalStack[-int(numberToMove[j]):])
    stack[int(targetStackNumber[j])-1] = stack[int(targetStackNumber[j])-1] + originalStack[-int(numberToMove[j]):] # add to target stack
    stack[int(startingStackNumber[j])-1] = originalStack[:-int(numberToMove[j])] # remove from original stack
    j += 1

print(stack)

for each in stack:
    print(each[-1])
