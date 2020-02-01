import sys
import math as m
import random 
# globals
T = 20
discov_count = 0

class node:
    def __init__(self,x,y,discov,adj_index):
        self.x = x
        self.y = y
        self.discov = discov
        self.adj_index = adj_index

    def display(self):
        print("x",self.x," y",self.y," discov",self.discov)
# ----------------------------------------------------------
def choose_random_neighbour(nodelist):
    n = len(nodelist)
    while(1):
        neighbour = nodelist[random.randrange(0,N)]
        if neighbour.discov == 0:
            return neighbour


def eval(c,n,adj):
    return adj[c.adj_index][n.adj_index]
    


def Probability(current,neighbour,adj):
    delE = eval(current,neighbour,adj)
    P = (    1/(1+ m.exp( delE/T ))     ) 
    return P

def monoton_decre_T(T):
    T = T * 0.9
    
def sim_anneal(current,nodelist,adj):
    global discov_count
    path = [current]
    steps = 0
    while(discov_count<=len(nodelist)-2):
        steps = 0
        while(steps < 5 and discov_count<=len(nodelist)-2):
            neighbour = choose_random_neighbour(nodelist)
            probab = Probability(current,neighbour,adj)
            print(probab)
            if (random.random() <= probab):
                neighbour.discov = 1
                discov_count += 1
                # print(discov_count)
                path.append(neighbour)
                current = neighbour
                steps += 1
        monoton_decre_T(T)
        # print("ZO",discov_count)
    return path


def path_cost(path,adj):
    current = path[0]
    cost = 0
    for i in range(1,len(path)):
        cost += eval(current,path[i],adj)
        current = path[i]
    return cost

















f = open(sys.argv[1],"r")

dist_type = f.readline().rstrip()
N = int(f.readline())

print(dist_type,N)

coords = [[None]*2]*N
adj = [[None]*N]*N

for i in range(0,N):
    coords[i] = list(map(lambda x: float(x), list(f.readline().rstrip().split(" "))))
for i in range(0,N):
    adj[i] = list(map(lambda x: float(x), list(f.readline().rstrip().split(" "))))

# for i in range(0,N):
#     print(coords[i])

# for i in range(0,N):
#     print(adj[i])

nodelist = [None]*N
for i in range(0,N):
    temp = node(coords[i][0],coords[i][1],0,i)
    nodelist[i] = temp


ori_cost = path_cost(nodelist,adj) #original cost

# random start city
current = choose_random_neighbour(nodelist)
current.discov = 1

path = sim_anneal(current,nodelist,adj)

print("ori_cost",ori_cost)
print("new_cost",path_cost(path,adj))





# print(choose_random_neighbour(nodelist).display())


# delE = 13
# T = 10
# print(  1/(1+ m.exp( (delE)/T  ) )    )