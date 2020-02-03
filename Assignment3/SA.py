import sys
import math as m
import random 
# globals
T = 90
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

def monoton_decre_T(k):
    global T
    if(int(sys.argv[2]) == 1):
        T = T * 0.90
    elif(int(sys.argv[2]) == 2):
        T = T/( 1 + m.log(1+k) )
    elif(int(sys.argv[2]) == 3):
        T = T /(1 + 0.5*k)

    
def sim_anneal(current,nodelist,adj):
    global discov_count
    path = [current]
    best_path = nodelist
    steps = 0
    k = 0
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
        if(path_cost(best_path,adj)>path_cost(path,adj)):
            best_path = path
        k += 1
        monoton_decre_T(k)
        print("ZO",T)
    return best_path


def path_cost(path,adj):
    current = path[0]
    cost = 0
    for i in range(1,len(path)):
        cost += eval(current,path[i],adj)
        current = path[i]
    return cost












if(int(sys.argv[2]) == 1):
    T = 95
elif(int(sys.argv[2]) == 2):
    T = 200000000000
elif(int(sys.argv[2]) == 3):
    T = 2000



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