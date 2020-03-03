# run as "python3 a_star.py <h_fun_id--1/2/3> file.txt"
import sys


class Node:   # creating node
    def __init__(self):
        self.value = 2   # values can be +,0,* or blank; modified--->0 for friend, 1 for enemy, 2 for blank, 3 for goal
        self.h = -1   # distance from goal in tree for friends, Heuristic
        self.g = -1     # g value of A*
        self.dis = -1  # distance from friend node (change)
        self.f = -1   # f-value of A*
        self.x = -1    # coordinate of node
        self.y = -1
        self.parent = None   # for revisiting path
        self.num = -1

    def __str__(self):   # printing
        return "("+str(self.x) + "," + str(self.y)+") " + str(self.num) + " g_value: " + str(self.g) + " h_value: " + str(self.h) + " f_value: " + str(self.f)
 # 0 for friend, 1 for enemy, 2 for blank, 3 for goal


def moveable_path(node):  # return neighbours of a node    --- using for bfs
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


def propagateimprovement(node):     # propagate Improvement for node in close
    neighbour = MoveGen(node)
    for temp in neighbour:
        dis = node.g + dist_matrix[node.num][temp.num]
        if dis < temp.g:        # comparing g value of child
            temp.parent = node  # updating
            temp.g = dis
            if temp in close:
                propagateimprovement(temp)  # doing for child of child


def MoveGen(kk):        # return child of node
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr[0])):
            array[i][j].dis = -1   # reinitialising distance

    queue = list()     # finding childs
    kk.dis = 0      # unitialisation
    neighbour = list()
    queue.append(kk)            # appling BFS
    while queue:
        temp = queue.pop(0)
        adjacent = moveable_path(temp)   # getting neighbours
        # removing already visited node
        adjacent = [node for node in adjacent if node.dis == -1]
        for node in adjacent:
            node.dis = temp.dis + 1   # updating distance
            if node.value == 0 or node.value == 3:
                neighbour.append(node)      # putting in neighbour
            else:
                queue.append(node)
    return neighbour


file = open(sys.argv[2], "r")    # opensing input file

temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()

array = list()  # list storing all values with node
friends = list()   # list having same team player
enemy = list()  # list having enemy team player

for i in range(len(temp_arr)):  # creating node and putting in array
    kk = []
    for j in range(len(temp_arr[0])):
        temp = Node()
        kk.append(temp)
    array.append(kk)

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
            temp.value = 3   # updating value for goal state
            temp.h = 0
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
for i in range(len(friends)):
    friends[i].num = i


# distance matrix
# distance of friend from each other
dist_matrix = [[-1]*len(friends)]*len(friends)
for t in range(len(friends)):
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr[0])):
            array[i][j].dis = -1   # reinitialising distance

    kk = friends[t]
    queue = list()     # finding childs
    kk.dis = 0
    queue.append(kk)
    while queue:
        temp = queue.pop(0)
        adjacent = moveable_path(temp)   # getting neighbours
        # removing already visited node
        adjacent = [node for node in adjacent if node.dis == -1]
        for node in adjacent:
            node.dis = temp.dis + 1   # updating distance
            queue.append(node)
    for temp in friends:
        # distance of each node from kk
        dist_matrix[kk.num][temp.num] = temp.dis


# defining Heuristic function
if sys.argv[1] == '3':
    # First Heuristic function based on euclidian distance---monotonic
    for node in friends:
        xx = node.x
        yy = node.y
        # eucledian formula
        euclidean_distance = ((goal_x-xx)**2 + (goal_y-yy) ** 2)**(0.5)
        node.h = euclidean_distance
elif sys.argv[1] == '1':  # overstimates
    area = row*col
    for node in friends:
        xx = node.x
        yy = node.y
        # node.h = area + abs(goal_x-xx)+abs(goal_y-yy) + \
        #     max(abs(goal_x-xx), abs(goal_y-yy))
        node.h = area + (goal_x-xx)**2+(goal_y-yy)**2 + \
            abs(goal_x-xx)+abs(goal_y-yy) + max(abs(goal_x-xx), abs(goal_y-yy))

elif sys.argv[1] == '2':         # mod distance ---understimate
    for node in friends:
        xx = node.x
        yy = node.y
        node.h = abs(goal_x-xx)+abs(goal_y-yy)      # Manhattan distance


finds = False   # target found or not
# time = 0     # count steps
opens = list()   # open list
close = list()   # closed list

start = array[0][0]
start.f = start.h
start.g = 0
start.parent = None
opens.append(start)

print("start visiting")
while not finds:
    kk = opens.pop(0)  # taking best from opens list
    print(kk)  # printing node visiting
    close.append(kk)   # putting in closed
    if kk.value == 3:  # checking goal
        finds = True   # goal found
        # time += 1
        break

    neighbour = MoveGen(kk)     # get child

    for node in neighbour:
        if node not in opens and node not in close:     # case first
            node.parent = kk
            node.g = kk.g+dist_matrix[kk.num][node.num]
            node.f = node.g + node.h                # new child , putting in open
            opens.append(node)
        elif node in opens:     # case second
            ss = kk.g + dist_matrix[kk.num][node.num]
            if ss < node.g:                         # comparing g value
                node.parent = kk
                node.g = ss
                node.f = node.g+node.h
        elif node in close:         # case third
            if kk.g + dist_matrix[kk.num][node.num] < node.g:       # comparing
                node.parent = kk
                node.g = dist_matrix[kk.num][node.num] + kk.g
                node.f = node.g+node.h
                propagateimprovement(node)      # updating child f

    opens.sort(key=lambda x: x.f)  # sorting opens based on distance
    if len(opens) == 0:
        print("No solution exits")
        break  # open becomes empty, No solution

# required returning path
print("\nprinting optimal path")
path = list()
end = array[goal_x][goal_y]
while(end != None):
    path.append(end)
    end = end.parent
path.reverse()
for i in path:
    print(i)
