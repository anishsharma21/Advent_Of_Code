infile = open('presents.txt')
moves = [move for move in infile.read()]

def modify_position(pos, char):
    if char == '^':
        pos[1] += 1
    elif char == 'v':
        pos[1] -= 1
    elif char == '<':
        pos[0] -= 1
    else:
        pos[0] += 1
    return pos

### Part 1
visited = {'00': 1}
pos = [0,0]
for move in moves:
    pos = modify_position(pos, move)
    house_position = str(pos[0]) + str(pos[1])
    if house_position in visited:
        visited[house_position] += 1
    else:
        visited[house_position] = 1
print(len(visited))

### Part 2
visited = {'00': 2}
santa_pos = [0,0]
robot_pos = [0,0]

for i in range(0, len(moves), 2):
    santa_pos = modify_position(santa_pos, moves[i])
    house_position = str(santa_pos[0]) + str(santa_pos[1])
    if house_position in visited:
        visited[house_position] += 1
    else:
        visited[house_position] = 1

for i in range(1, len(moves), 2):
    robot_pos = modify_position(robot_pos, moves[i])
    house_position = str(robot_pos[0]) + str(robot_pos[1])
    if house_position in visited:
        visited[house_position] += 1
    else:
        visited[house_position] = 1

print(len(visited))