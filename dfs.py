class Node:
    def __init__(self):
        self.value = ''
        self.color = 'white'
        self.dis = -1
        self.parent = None
        self.x = -1
        self.y = -1

    def __str__(self):
        return self.value + " " + str(self.x) + " " + str(self.y) + " dis: " + str(self.dis)


def get_adjacent(node):  # return neighbours of a node
    xx = node.x
    yy = node.y
    # print(xx, yy)
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
    adjacent = adjacent[::-1]
    return adjacent


def dfs_visit(node):
    global finds
    # global count
    # print("visiting:  node is:")
    # print(node)
    # print("parent is: ")
    # print(node.parent)
    node.color = 'gray'
    # count += 1
    # print(count)
    if node.x == goal_x and node.y == goal_y:
        # print("Done\n")
        node.color = 'black'
        finds = True
        return
    adjacent = get_adjacent(node)
    adjacent = [temp for temp in adjacent if temp.color == 'white']

    for temp in adjacent:
        temp.color = 'gray'
    # print("No of neighbours: ", len(adjacent))
    # print("\n")
    for temp in adjacent:
        if finds:
            break
        temp.parent = node
        temp.dis = node.dis+1
        dfs_visit(temp)
    node.color = 'black'


file = open("input.txt", "r")
types = file.readline()[0]    # types means bfs, dfs or dfid
# print(types)
temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()
array = list()  # list storing all values with node
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
# print("Dimension is:", row, col)
# print("starting from node at", array[0][0].x, array[0][0].y)
# print("Goal is : ", goal_x, goal_y)
# print("\n")

array[0][0].color = 'gray'
array[0][0].dis = 1
count = 0  # count number of visited node

finds = False
dfs_visit(array[0][0])

path = list()
for i in range(len(temp_arr)):
    kk = [1]*len(temp_arr[0])
    path.append(kk)

temp = array[goal_x][goal_y]
# print(temp.value)
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
cc = 0
for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j].color == 'black':
            cc += 1

with open("output.txt", "w") as ff:
    ff.write(str(cc))
    ff.write("\n")
    ff.write(str(array[goal_x][goal_y].dis))
    ff.write("\n")
    for i in range(len(path)):
        kk = "".join(path[i])
        ff.write(kk)
        ff.write("\n")


# print("counting.....", cc, "\n\n")
