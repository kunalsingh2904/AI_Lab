import sys


class Node:    # creating node
    def __init__(self):
        self.value = ''     # values can be +,-,|,* or blank
        self.color = 'white'
        self.dis = -1     # distance from [0][0] in tree
        self.parent = None
        self.x = -1         # coordinate of node
        self.y = -1

    def __str__(self):   # printing
        return "visiting node at" + " " + str(self.x) + " " + str(self.y) + " at dis: " + str(self.dis)


def MoveGen(node):  # return neighbours of a node
    xx = node.x
    yy = node.y
    adjacent = []
    kk = ['+', '-', '|']
    if xx+1 < row and array[xx+1][yy].value not in kk:   # Down
        adjacent.append(array[xx+1][yy])
    if xx-1 >= 0 and array[xx-1][yy].value not in kk:     # Top
        adjacent.append(array[xx-1][yy])
    if yy+1 < col and array[xx][yy+1].value not in kk:     # Right
        adjacent.append(array[xx][yy+1])
    if yy-1 >= 0 and array[xx][yy-1].value not in kk:    # Left
        adjacent.append(array[xx][yy-1])
    # adjacent = adjacent[::-1]      # for alternating solution
    return adjacent


def dfs_visit(node):   # dfs visit for  node
    global finds
    node.color = 'gray'    # visiting
    if node.x == goal_x and node.y == goal_y:   # checking for target node
        node.color = 'black'
        finds = True
        return
    adjacent = MoveGen(node)    # finding neighbours
    # remove visited node
    adjacent = [temp for temp in adjacent if temp.color == 'white']
    for temp in adjacent:
        temp.color = 'gray'
    for temp in adjacent:
        if finds:
            break
        temp.parent = node        # assigning parent
        temp.dis = node.dis+1     # updating distance
        dfs_visit(temp)      # visiting child
    node.color = 'black'    # marking visited


file = open(sys.argv[1], "r")    # opening input file
types = file.readline()[0]    # types means bfs, dfs or dfid

temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()
array = list()  # list storing all values with node
for i in range(len(temp_arr)):   # creating node and putting in array
    kk = []
    for j in range(len(temp_arr[0])):
        temp = Node()
        kk.append(temp)
    array.append(kk)

goal_x = -1
goal_y = -1
for i in range(len(temp_arr)):  # assigning location and value to each node
    for j in range(len(temp_arr[0])):
        temp = array[i][j]
        temp.value = temp_arr[i][j]
        temp.x = i
        temp.y = j
        if temp_arr[i][j] == '*':    # finding location of target node
            goal_x = i
            goal_y = j


row = len(array)
col = len(array[0])  # dimension of array

array[0][0].color = 'gray'
array[0][0].dis = 1

finds = False     # found Target
dfs_visit(array[0][0])    # start dfs

path = list()    # list for path tracing
for i in range(len(temp_arr)):
    kk = [1]*len(temp_arr[0])
    path.append(kk)

temp = array[goal_x][goal_y]
while(temp is not None):    # creating path
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

cc = 0   # counting visited node
for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j].color == 'black':
            cc += 1

with open("output.txt", "w") as ff:    # output file
    ff.write(str(cc))    # writing desired outputs
    ff.write("\n")
    ff.write(str(array[goal_x][goal_y].dis))
    ff.write("\n")
    for i in range(len(path)):
        kk = "".join(path[i])
        ff.write(kk)
        ff.write("\n")
