# set checker
def uniqueCheck(inputA, inputB, inputC, inputD):
    originalSet = [inputA, inputB, inputC, inputD]
    seen = set()

    for input in originalSet:
        if input not in seen:
            seen.add(input)
        else: # duplicate
            return False
    return True # it's a unique set

input = open("input.txt", "r")
text = input.readline()

i = 0
unique = False

while not unique:
    unique = uniqueCheck(text[i], text[i+1], text[i+2], text[i+3])
    i += 1

packetStart = i + 3
print("Start of packet is", packetStart)
