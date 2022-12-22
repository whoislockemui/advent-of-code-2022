input = open("input.txt", "r")
text = input.readline()

i = 0

while i < len(text):
    if len(set(text[i:i+14])) == 14:
        print("Start of message is", i + 14)
        exit()
    i += 1
