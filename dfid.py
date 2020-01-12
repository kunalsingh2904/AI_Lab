import sys


class Node:
    def __init__(self):
        self.value = ''
        self.dis = -1
        self.parent = None
        self.x = -1
        self.y = -1

    def __str__(self):
        return self.value + " " + str(self.x) + " " + str(self.y) + " dis: " + str(self.dis)


def get_adjacent(node):  # return neighbours of a node
    xx = node.x
    yy = node.y
    adjacent = []
    kk = ['+', '-', '|']
    if xx+1 < row and array[xx+1][yy].value not in kk:
        adjacent.append(array[xx+1][yy])
    if xx-1 >= 0 and array[xx-1][yy].value not in kk:
        adjacent.append(array[xx-1][yy])
    if yy+1 < col and array[xx][yy+1].value not in kk:
        adjacent.append(array[xx][yy+1])
    if yy-1 >= 0 and array[xx][yy-1].value not in kk:
        adjacent.append(array[xx][yy-1])
    return adjacent


def dfs_visit(node):
    global finds
    goal.dis += 1
    if node.x == goal_x and node.y == goal_y:
        finds = True
        return

    if node.dis - 1 == depth:
        return
    adjacent = get_adjacent(node)
    for temp in adjacent:
        if finds:
            break
        if temp.dis is -1:
            temp.parent = node
            temp.dis = node.dis+1
            dfs_visit(temp)
        elif temp.dis > node.dis + 1:
            temp.parent = node
            temp.dis = node.dis+1
            dfs_visit(temp)


file = open(sys.argv[1], "r")
types = file.readline()    # types means bfs, dfs or dfid
# print(types)
temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()
array = list()
for i in range(len(temp_arr)):
    kk = []
    for j in range(len(temp_arr[0])):
        temp = Node()
        kk.append(temp)
    array.append(kk)

goal_x = -1
goal_y = -1
for i in range(len(temp_arr)):
    for j in range(len(temp_arr[0])):
        temp = array[i][j]
        temp.value = temp_arr[i][j]
        temp.x = i
        temp.y = j
        if temp_arr[i][j] == '*':
            goal_x = i
            goal_y = j

row = len(array)
col = len(array[0])
finds = False
depth = 0


goal = Node()
goal.dis = 0

if array[0][0].x == goal_x and array[0][0].y == goal_y:
    goal.dis = 1
    finds = True

while not finds:
    depth += 1
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr[0])):
            array[i][j].dis = -1

    array[0][0].dis = 1

    dfs_visit(array[0][0])
    # print("depth: {0} and visit: {1}\n".format(depth, goal.dis))

path = list()
for i in range(len(temp_arr)):
    kk = [1]*len(temp_arr[0])
    path.append(kk)

temp = array[goal_x][goal_y]
while(temp is not None):
    xx = temp.x
    yy = temp.y
    path[xx][yy] = 0
    temp = temp.parent

for i in range(len(temp_arr)):
    for j in range(len(temp_arr[0])):
        if path[i][j] == 1:
            path[i][j] = temp_arr[i][j]
        else:
            path[i][j] = '0'

with open("output.txt", "w") as ff:
    ff.write(str(goal.dis))
    ff.write("\n")
    ff.write(str(array[goal_x][goal_y].dis))
    ff.write("\n")
    for i in range(len(path)):
        kk = "".join(path[i])
        ff.write(kk)
        ff.write("\n")
