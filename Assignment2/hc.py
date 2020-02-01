# run as "python3 hc.py <h_fun_id--1/2> file.txt"
import sys


class Node:   # creating node
    def __init__(self):
        self.value = 2   # values can be +,0,* or blank; modified--->0 for friend, 1 for enemy, 2 for blank, 3 for goal
        self.d = -1   # distance from goal in tree for friends
        self.dis = -1  # distance from friend node (change)
        self.x = -1    # coordinate of node
        self.y = -1
        self.parent = None

    def __str__(self):   # printing
        return str(self.x) + " " + str(self.y) + " distance: " + str(self.d)
 # 0 for friend, 1 for enemy, 2 for blank, 3 for goal


def MoveGen(node):  # return neighbours of a node
    xx = node.x
    yy = node.y
    adjacent = []
    if xx+1 < row and array[xx+1][yy].value != 1:  # Down
        adjacent.append(array[xx+1][yy])
    if xx-1 >= 0 and array[xx-1][yy].value != 1:   # Top
        adjacent.append(array[xx-1][yy])
    if yy+1 < col and array[xx][yy+1].value != 1:  # Right
        adjacent.append(array[xx][yy+1])
    if yy-1 >= 0 and array[xx][yy-1].value != 1:   # Left
        adjacent.append(array[xx][yy-1])
    return adjacent


file = open(sys.argv[2], "r")    # opensing input file

temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()

# list storing all values with node
# creating node and putting in array
array = [[Node() for j in range(len(temp_arr[0]))]
         for i in range(len(temp_arr))]

friends = list()   # list having same team player
enemy = list()  # list having enemy team player

goal_x = -1   # coordinate of goal state
goal_y = -1

for i in range(len(temp_arr)):  # assigning location and value to each node
    for j in range(len(temp_arr[0])):
        temp = array[i][j]
        temp.x = i      # assigning coordinates
        temp.y = j
        if temp_arr[i][j] == '*':   # finding location of target node
            goal_x = i
            goal_y = j
            temp.value = 3      # marking as goal node
            temp.d = 0
            friends.append(temp)
        elif temp_arr[i][j] == '0':  # finding friends
            temp.value = 0
            friends.append(temp)
        elif temp_arr[i][j] == '+':  # finding enemy
            temp.value = 1
            enemy.append(temp)
        else:                   # normal node
            temp.value = 2


row = len(array)   # dimension of array
col = len(array[0])


for node in enemy:    # ball can't be pass by enemy neighbours
    xx = node.x
    yy = node.y
    if xx+1 < row:                      # down
        array[xx+1][yy].value = 1
    if xx-1 >= 0:                       # up
        array[xx-1][yy].value = 1
    if yy+1 < col:                          # right
        array[xx][yy+1].value = 1
    if yy-1 >= 0:                       # left
        array[xx][yy-1].value = 1
    if xx-1 >= 0 and yy-1 >= 0:             # up left diigonal
        array[xx-1][yy-1].value = 1
    if xx-1 >= 0 and yy+1 < col:            # up right diigonal
        array[xx-1][yy+1].value = 1
    if xx+1 < row and yy-1 >= 0:            # down left diigonal
        array[xx+1][yy-1].value = 1
    if xx+1 < row and yy+1 < col:           # down right diigonal
        array[xx+1][yy+1].value = 1


# removing un-useful friends
friends = [node for node in friends if node.value == 0 or node.value == 3]

# defining Heuristic function
if sys.argv[1] == '1':
    # First Heuristic function based on euclidian distance
    for node in friends:
        xx = node.x
        yy = node.y
        euclidean_distance = ((goal_x-xx)**2 + (goal_y-yy)
                              ** 2)**(0.5)  # euclidean formula
        node.d = euclidean_distance
elif sys.argv[1] == '2':
    # second Heuristic function based on path length
    queue2 = list()
    array[goal_x][goal_y].d = 0
    queue2.append(array[goal_x][goal_y])
    while queue2:
        temp = queue2.pop(0)
        adjacent = MoveGen(temp)   # getting neighbours
        # removing already visited node
        adjacent = [node for node in adjacent if node.d == -1]
        for node in adjacent:
            node.d = temp.d + 1   # updating distance
            queue2.append(node)


finds = False       # found target or not
time = 0            # count no. of steps
opens = list()      # open list
close = list()      # close list
store = list()      # temprory list to store all node
opens.append(array[0][0])
while not finds:
    for node in opens:      # storing in store to avoid repeatation
        store.append(node)
    kk = opens.pop(0)  # taking best from opens list
    print(kk)  # printing node visiting
    close.append(kk)
    opens.clear()
    if kk.value == 3:    # goal test
        finds = True        # found target
        time += 1
        break
    queue = list()
    kk.dis = 1
    queue.append(kk)
    while queue:            # bfs to find child
        temp = queue.pop(0)
        time += 1       # updating counts
        adjacent = MoveGen(temp)   # getting neighbours
        # removing already visited node
        adjacent = [node for node in adjacent if node.dis == -1]
        for node in adjacent:
            node.dis = temp.dis + 1   # updating distance
            node.parent = temp        # assigning parent
            if node.value == 0 or node.value == 3:
                opens.append(node)   # child
            else:
                queue.append(node)

    # removing already visited node
    opens = [node for node in opens if node not in store]
    opens.sort(key=lambda x: x.d)  # sorting opens based on distance
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr[0])):  # reinitializing distance
            array[i][j].dis = -1
    # child must be better than parent node
    if len(opens) == 0 or kk.d < opens[0].d:
        print("\nproblem. can't find path.\n")
        break

# required output
print("\nTotal node explored: {0}".format(len(store)))
print("Total time taken in term of steps: {0} ".format(time))
