input = open("input.txt", "r")

pwd = [] # keep track of where we are
sizeMap = {}

for line in input:
    if "$ cd" in line: # we're moving into a dir
        _, _, dir = line.split()
        if dir == "..":
            pwd = pwd[:-1] # remove a directory from path
        else:
            pwd.append(dir) # add directory to path
            sizeMap.update({'/'.join(pwd): 0}) # this is a new path, add to sizeMap dictionary
    elif "$ ls" in line: # doesn't do anything for us
        continue
    else: # it's one of the items in the ls
        size, fileName = line.split() # size can be 'dir' or the actual filesize
        if size.isdigit():
            for n in range(1, len(pwd) + 1):    # parent directories and directory get size added
                sizeMap['/'.join(pwd[0:n])] += int(size)

totalSize = 0

for item in sizeMap:
    if sizeMap[item] < 100000:
        totalSize += sizeMap[item]

print(totalSize)
