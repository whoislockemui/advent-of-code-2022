input = open("input.txt", "r")

totalOverlap = 0

for line in input:
    partners = line.strip().split(',')
    partnerOne = partners[0].split('-')
    partnerTwo = partners[1].split('-')

    A = int(partnerOne[0])
    B = int(partnerOne[1])
    C = int(partnerTwo[0])
    D = int(partnerTwo[1])

    if (A >= C and A <= D and B <= D) or \
       (C >= A and C <= B and D <= B) or \
       (A <= C and B <= D and B >= C) or \
       (C <= A and D <= B and D >= A):
        totalOverlap += 1

print(totalOverlap)
