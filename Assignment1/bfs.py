import sys


class Node:   # creating node
    def __init__(self):
        self.value = ''     # values can be +,-,|,* or blank
        self.color = 'white'
        self.dis = -1  # distance from [0][0] in tree
        self.parent = None
        self.x = -1    # coordinate of node
        self.y = -1

    def __str__(self):   # printing
        return self.value + " " + str(self.x) + " " + str(self.y) + " dis: " + str(self.dis)


def MoveGen(node):  # return neighbours of a node
    xx = node.x
    yy = node.y
    adjacent = []
    kk = ['+', '-', '|']
    if xx+1 < row and array[xx+1][yy].value not in kk:  # Down
        adjacent.append(array[xx+1][yy])
    if xx-1 >= 0 and array[xx-1][yy].value not in kk:   # Top
        adjacent.append(array[xx-1][yy])
    if yy+1 < col and array[xx][yy+1].value not in kk:  # Right
        adjacent.append(array[xx][yy+1])
    if yy-1 >= 0 and array[xx][yy-1].value not in kk:   # Left
        adjacent.append(array[xx][yy-1])
    return adjacent


file = open(sys.argv[1], "r")    # opening input file
types = file.readline()    # types means bfs, dfs or dfid

temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()

array = list()  # list storing all values with node
for i in range(len(temp_arr)):  # creating node and putting in array
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
        if temp_arr[i][j] == '*':   # finding location of target node
            goal_x = i
            goal_y = j

row = len(array)   # dimension of array
col = len(array[0])

array[0][0].color = 'gray'
array[0][0].dis = 1

queue = list()    # creating queue for bfs
count = 0  # count visited node
queue.append(array[0][0])

while queue:
    temp = queue.pop(0)
    count += 1
    adjacent = MoveGen(temp)   # getting neighbours
    # removing already visited node
    adjacent = [node for node in adjacent if node.color == 'white']
    for node in adjacent:
        node.color = 'gray'
        node.dis = temp.dis + 1   # updating distance
        node.parent = temp        # assigning parent
        queue.append(node)
    temp.color = 'black'
    if temp.x == goal_x and temp.y == goal_y:  # checking for target
        break

# Tracing path
path = list()
for i in range(len(temp_arr)):
    kk = [1]*len(temp_arr[0])
    path.append(kk)
temp = array[goal_x][goal_y]
while(temp is not None):   # creating path
    xx = temp.x
    yy = temp.y
    path[xx][yy] = 0
    temp = temp.parent
for i in range(len(temp_arr)):
    for j in range(len(temp_arr[0])):     # writing 0 as value for node in path
        if path[i][j] == 1:
            path[i][j] = temp_arr[i][j]
        else:
            path[i][j] = '0'

with open("output.txt", "w") as ff:   # output file
    ff.write(str(count))                # writing desired outputs
    ff.write("\n")
    ff.write(str(array[goal_x][goal_y].dis))
    ff.write("\n")
    for i in range(len(path)):
        kk = "".join(path[i])
        ff.write(kk)
        ff.write("\n")
