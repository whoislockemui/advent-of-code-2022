input = open("input.txt", "r")

totalOverlap = 0

for line in input:
    partners = line.strip().split(',')
    partnerOne = partners[0].split('-')
    partnerTwo = partners[1].split('-')

    if (partnerOne[0] >= partnerTwo[0] and partnerOne[0] <= partnerTwo[1] and partnerOne[1] <= partnerTwo[1]) or \
       (partnerTwo[0] >= partnerOne[0] and partnerTwo[0] <= partnerOne[1] and partnerTwo[1] <= partnerOne[1]):
        totalOverlap += 1

print(totalOverlap)
