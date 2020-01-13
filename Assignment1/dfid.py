import sys


class Node:      # creating node
    def __init__(self):
        self.value = ''     # values can be +,-,|,* or blank
        self.dis = -1        # distance from [0][0] in tree
        self.parent = None
        self.x = -1       # coordinate of node
        self.y = -1

    def __str__(self):   # printing
        return self.value + " " + str(self.x) + " " + str(self.y) + " dis: " + str(self.dis)


def MoveGen(node):  # return neighbours of a node
    xx = node.x
    yy = node.y
    adjacent = []
    kk = ['+', '-', '|']
    if xx+1 < row and array[xx+1][yy].value not in kk:    # Down
        adjacent.append(array[xx+1][yy])
    if xx-1 >= 0 and array[xx-1][yy].value not in kk:    # Top
        adjacent.append(array[xx-1][yy])
    if yy+1 < col and array[xx][yy+1].value not in kk:     # Right
        adjacent.append(array[xx][yy+1])
    if yy-1 >= 0 and array[xx][yy-1].value not in kk:    # Left
        adjacent.append(array[xx][yy-1])
    # adjacent = adjacent[::-1]      # for alternating solution
    return adjacent


def dfs_visit(node):    # dfs visit for  node
    global finds
    goal.dis += 1
    if node.x == goal_x and node.y == goal_y:   # checking for target node
        finds = True
        return

    if node.dis - 1 == depth:   # chcking  max depth allowed
        return
    adjacent = MoveGen(node)     # finding neighbours
    for temp in adjacent:
        if finds:
            break
        if temp.dis is -1:   # not visited node
            temp.parent = node  # assigning parent
            temp.dis = node.dis+1        # updating distance
            dfs_visit(temp)   # visiting child
        elif temp.dis > node.dis + 1:   # checking for optimisation
            temp.parent = node     # assigning new parent
            temp.dis = node.dis+1       # updating distance
            dfs_visit(temp)   # visiting again


file = open(sys.argv[1], "r")    # opening input file
types = file.readline()    # types means bfs, dfs or dfid
# print(types)
temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()
array = list()   # list storing all values with node
for i in range(len(temp_arr)):   # creating node and putting in array
    kk = []
    for j in range(len(temp_arr[0])):
        temp = Node()
        kk.append(temp)
    array.append(kk)

goal_x = -1
goal_y = -1
for i in range(len(temp_arr)):   # assigning location and value to each node
    for j in range(len(temp_arr[0])):
        temp = array[i][j]
        temp.value = temp_arr[i][j]
        temp.x = i
        temp.y = j
        if temp_arr[i][j] == '*':    # finding location of target node
            goal_x = i
            goal_y = j

row = len(array)   # dimension of array
col = len(array[0])

finds = False
depth = 0  # depth of dfs allowed


goal = Node()  # counts visited node
goal.dis = 0

if array[0][0].x == goal_x and array[0][0].y == goal_y:
    goal.dis = 1       # checking initial as target node
    array[0][0].dis = 1
    finds = True

while not finds:   # dfid starts with upgrading depth
    depth += 1
    for i in range(len(temp_arr)):   # reassigning each node
        for j in range(len(temp_arr[0])):
            array[i][j].dis = -1

    array[0][0].dis = 1

    dfs_visit(array[0][0])   # dfs visit of node


path = list()  # list for path tracing
for i in range(len(temp_arr)):
    kk = [1]*len(temp_arr[0])
    path.append(kk)

temp = array[goal_x][goal_y]
while(temp is not None):  # creating path
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

with open("output.txt", "w") as ff:  # output file
    ff.write(str(goal.dis))   # writing desired outputs
    ff.write("\n")
    ff.write(str(array[goal_x][goal_y].dis))
    ff.write("\n")
    for i in range(len(path)):
        kk = "".join(path[i])
        ff.write(kk)
        ff.write("\n")
