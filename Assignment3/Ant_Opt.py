import sys
import math as m
import random 


class best:
    def __init__(self,cost,path):
        self.cost = cost
        self.path = path





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


def cost(c,n,adj):
    return adj[c.adj_index][n.adj_index]
def pheromone(c,n,Tau_Matrix):
    return Tau_Matrix[c.adj_index][n.adj_index]


def probab(current,neighbour,nodelist,adj,Tau_Matrix):
    Tau = pheromone(current,neighbour,adj)
    Eta = 1/(cost(current,neighbour,Tau_Matrix))

    sum_Tau_Eta = 1
    alpha = 1
    beta = 1
    for i in range(0,len(nodelist)):
        if nodelist[i].discov == 0 and nodelist[i] != current:
            sum_Tau_Eta += pheromone(current,nodelist[i],Tau_Matrix)**alpha * (1/(cost(current,nodelist[i],Tau_Matrix)))**beta


    return  (  Tau**alpha * Eta**beta   )/(   sum_Tau_Eta      )




def path_cost(path,adj):
    current = path[0]
    cost_p = 0
    for i in range(1,len(path)):
        cost_p += cost(current,path[i],adj)
        current = path[i]
    return cost_p


def update_path_pheromones(path,Tau_Matrix,adj):
        Rho = 0.6 ##evaporation coefficient
        Q = 10 #costant
        delTau = Q/path_cost(path,adj)

        for i in range(0,len(path)-1):
            Tau_Matrix[path[i].adj_index][path[i+1].adj_index] = (1 - Rho) * Tau_Matrix[path[i].adj_index][path[i+1].adj_index] + delTau


def make_tour(current,nodelist,adj,Tau_Matrix):
    for node in nodelist:
        node.discov = 0
    discov_count = 0
    path = [current] #path of kth Ant
    while(discov_count <= len(nodelist)-2):
        neighbour = choose_random_neighbour(nodelist)
        probability = probab(current,neighbour,nodelist,adj,Tau_Matrix)
        if random.random() <= probability :
            neighbour.discov = 1
            discov_count += 1
            path.append(neighbour)
            current = neighbour
    return path
    






def Ant_Opt(nodelist,adj,Tau_Matrix,m_ants):
    current = nodelist[0]
    best_path = best(float('inf'),[None]*len(nodelist))
    conv_path  = [None]*2
    ind = 0
    for z in range(1,10):  #this counter to be updated later with convergence criterion i.e same path getting repeated
        for i in range (0,m_ants):
            kth_path = make_tour(current,nodelist,adj,Tau_Matrix)

            if path_cost(kth_path,adj) < best_path.cost:    #update best path
                best_path.cost = path_cost(kth_path,adj)
                best_path.path = kth_path

            update_path_pheromones(kth_path,Tau_Matrix,adj)    # Update pheromones of each edge of this path after the tour
    return best_path














f = open(sys.argv[1],"r")

dist_type = f.readline().rstrip()
N = int(f.readline())

print(dist_type,N)

coords = [[None]*2]*N
adj = [[None]*N]*N
Tau_Matrix = [[1]*N]*N #Pheromone depositite inititially with 1


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

m_ants = 100
b = Ant_Opt(nodelist,adj,Tau_Matrix,m_ants)
print(path_cost(nodelist,adj))
print(b.cost)






