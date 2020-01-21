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

def best(adja,parent):
    adj = []
    for i in adja:
        if(i.dis == -1  ):
            adj.append(i)
    adj.sort(key=lambda x: x.d)
    # for i in adj:
    #     print("ZZZZZZ",i.x," ",i.y," ",i.d ," ",parent.d)
    temp = []
    if(len(adj) != 0):
        if(adj[0].d <= parent.d or adj[0].d == 0 ):
            temp.append(adj[0])

    return temp

def VND(node):
    adj = []
    ind = 0
    while(len(adj) < 1 or MoveGen(node) == None ):
        adj = (best(MoveGen(node),node))
        # print("MM ",len(adj))

        temp = MoveGen(node)
        temp.sort(key=lambda x: x.d)
        node = temp[0]
        ind = ind + 1
        # print("||||||||||||",len(adj)," ",adj[0].x," ",adj[0].y)
    return adj

file = open("input.txt", "r")    # opensing input file

temp_arr = list()  # temporary list having input values
for line in file:
    line = line[0:(len(line)-1)]
    temp_arr.append(line)
file.close()
nm = len(temp_arr)*len(temp_arr[0])

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
        temp.x = i
        temp.y = j
        if temp_arr[i][j] == '*':   # finding location of target node
            goal_x = i
            goal_y = j
            temp.value = 3
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

# print(len(friends))
# print(len(enemy))
# print(goal_x, goal_y)


for node in enemy:    # ball can't be pass by enemy neighbours
    xx = node.x
    yy = node.y
    if xx+1 < row:
        array[xx+1][yy].value = 1
    if xx-1 >= 0:
        array[xx-1][yy].value = 1
    if yy+1 < col:
        array[xx][yy+1].value = 1
    if yy-1 >= 0:
        array[xx][yy-1].value = 1
    if xx-1 >= 0 and yy-1 >= 0:
        array[xx-1][yy-1].value = 1
    if xx-1 >= 0 and yy+1 < col:
        array[xx-1][yy+1].value = 1
    if xx+1 < row and yy-1 >= 0:
        array[xx+1][yy-1].value = 1
    if xx+1 < row and yy+1 < col:
        array[xx+1][yy+1].value = 1

# removing unuseful friends
friends = [node for node in friends if node.value == 0 or node.value == 3]

# defining Heuristic function
if sys.argv[1] == '1':
    # First Heuristic function based on euclidian distance
    for li in array:    
        for node in li:
            xx = node.x
            yy = node.y
            euclidean_distance = ((goal_x-xx)**2 + (goal_y-yy)**2)**(0.5)
            node.d = euclidean_distance
elif sys.argv[1] == '2':
    # second Heuristic function based on path length
    queue2 = list()
    array[goal_x][goal_y].d = 1
    queue2.append(array[goal_x][goal_y])
    while queue2:
        temp = queue2.pop(0)
        adjacent = MoveGen(temp)   # getting neighbours
        # removing already visited node
        adjacent = [node for node in adjacent if node.d == -1]
        for node in adjacent:
            node.d = temp.d + 1   # updating distance
            queue2.append(node)


finds = False
time = 0
opens = list()
close = list()
store = list()
opens.append(array[0][0])
while not finds:
    for node in opens:
        store.append(node)
    kk = opens.pop(0)  # taking best from opens list
    print(kk)  # printing node visiting
    close.append(kk)
    opens.clear()
    if kk.value == 3:
        finds = True
        time += 1
        break
    queue = list()
    kk.dis = 1
    queue.append(kk)
    while queue:
        temp = queue.pop(0)
        time += 1
        adjacent = VND(temp)  # getting neighbours
        # removing already visited node
        # print("++++++++++ ",adjacent[0].x," ",adjacent[0].y)
        adjacent = [node for node in adjacent if node.dis == -1]
        for node in adjacent:
            node.dis = temp.dis + 1   # updating distance
            node.parent = temp        # assigning parent
            if node.value == 0 or node.value == 3:
                opens.append(node) #opens for target 3 and friends 0
            else:
                queue.append(node) #queue for blank nodes empty field
    opens = [node for node in opens if node not in store]
    # print("----- ",len(opens))
    # opens.sort(key=lambda x: x.d)  # sorting opens based on distance
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr[0])):
            array[i][j].dis = -1
    if len(opens) == 0 or kk.d < opens[0].d and opens[0].d != 0:
        print("\nproblem. can't find path.\n")
        break


print("\nTotal node explored: {0}".format(len(opens)+len(close)))
print("Total time taken in term of steps: {0} ".format(time))
