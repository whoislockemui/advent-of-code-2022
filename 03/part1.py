input = open("input.txt", "r")

priority = 0

for line in input:
    first, second = line[:len(line)//2], line[len(line)//2:]
    common = ''.join(set(first).intersection(second))
    if common.islower():
        priority += (ord(common) - 96)
    else:
        priority += (ord(common) - 38)
    
print(priority)
