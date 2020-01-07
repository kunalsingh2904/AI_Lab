class Node:
    def __init__(self):
        self.value = ''
        self.color = 'white'
        self.dis = -1
        self.parent = None
        self.x = -1
        self.y = -1

    def __str__(self):
        return self.value + str(self.x) + " " + str(self.y)


def get_adjacent(node):  # return neighbours of a node
    xx = node.x
    yy = node.y
    print(xx, yy)
    adjacent = []
    if xx-1 >= 0:
        adjacent.append(array[xx-1][yy])
    if xx+1 < row:
        adjacent.append(array[xx+1][yy])
    if yy-1 >= 0:
        adjacent.append(array[xx][yy-1])
    if yy+1 < col:
        adjacent.append(array[xx][yy+1])
    return adjacent


file = open("input.txt", "r")
temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)

# print(temp_arr)
array = list()  # list storing all values with node
for i in range(len(temp_arr)):
    temps = [Node()]*len(temp_arr[0])
    array.append(temps)

goal_x = -1
goal_y = -1
for i in range(len(temp_arr)):
    for j in range(len(array[0])):
        array[i][j].value = temp_arr[i][j]
        array[i][j].x = i
        array[i][j].y = j
        if temp_arr[i][j] == '*':
            goal_x = i
            goal_y = j

row = len(array)
col = len(array[0])
# print("Dimension is:", row, col)
# print("starting from node at", array[0][0].x, array[0][0].y)

array[0][0].color = 'gray'
array[0][0].dis = 1
array[0][0].parent = None
print(temp_arr[0][0])
print(array[0][0].value)

queue = list()
count = 1  # count visited node
print(array[0][0])
queue.append(array[0][0])
# print(queue[0].x, queue[0].y)
while queue:
    temp = queue.pop(0)
    print("visiting node at", temp.x, temp.y)
    adjacent = get_adjacent(temp)
    print(len(adjacent))
    for node in adjacent:
        if node.color == 'white' and node.value not in ['+', '*', '-', '|']:
            node.color = 'gray'
            node.dis = temp.dis + 1
            node.parent = temp
            queue.append(node)
            count += 1
    temp.color = 'black'

print("Done\n")
print(count)
print(array[goal_x][goal_y].dis)
