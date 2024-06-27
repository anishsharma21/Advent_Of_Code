file = open('floors.txt', 'r')
characters = [char for char in file.read()]
floor = 0
for char in characters:
    if char == "(":
        floor += 1
    else:
        floor -= 1
print(floor)