input = open("input.txt", "r")

priority = 0

for line in input:
    lineTwo = input.readline().strip()
    lineThree = input.readline().strip()

    common = ''.join(set(line).intersection(lineTwo))
    finalCommon = ''.join(set(common).intersection(lineThree))

    if finalCommon.islower():
        priority += (ord(finalCommon) - 96)
    else:
        priority += (ord(finalCommon) - 38)

print(priority)
