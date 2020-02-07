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
def choose_random_neighbour(nodelist): #choose random neighbour with probability = 1/N
    n = len(nodelist)
    while(1):
        neighbour = nodelist[random.randrange(0,N)]
        if neighbour.discov == 0:
            return neighbour


def cost(c,n,adj):
    return adj[c.adj_index][n.adj_index]
def pheromone(c,n,Tau_Matrix):
    return Tau_Matrix[c.adj_index][n.adj_index]


def probab(current,neighbour,nodelist,adj,Tau_Matrix):  #return probability of (current,neighbour) by the given formula
    
   
    sum_Tau_Eta = 0
    alpha = 0.5
    beta = 1.2
    Tau_ = pheromone(current,neighbour,Tau_Matrix) ** alpha
    Eta_ = 1/(cost(current,neighbour,adj)) ** beta
    
    for i in range(0,len(nodelist)):
        if nodelist[i].discov == 0 :
            sum_Tau_Eta += (pheromone(current,nodelist[i],Tau_Matrix)**alpha) * (   (1/(cost(current,nodelist[i],adj)))**beta    )

    # print(sum_Tau_Eta ," ", Tau ," ", Eta)
    if sum_Tau_Eta == 0:
        return 1
    p = (  Tau_* Eta_   )/(   sum_Tau_Eta      )
    return  p




def path_cost(path,adj):    #cost of the tour path including return to start city
    current = path[0]
    cost_p = 0
    for i in range(1,len(path)):
        cost_p += cost(current,path[i],adj)
        current = path[i]
    return cost_p + cost(path[len(path)-1],path[0],adj)


def update_path_pheromones(path,Tau_Matrix,adj):    #after an ant has toured update the city/nodes with pheromones by given formula
        Rho = 0.4 ##evaporation coefficient
        Q = 1000 #costant
        delTau = Q/path_cost(path,adj)



        for i in range(0,len(Tau_Matrix)):
            for j in range(0,len(Tau_Matrix)):
                    Tau_Matrix[i][j] = (1 - Rho) * Tau_Matrix[i][j] + 0
 

        for i in range(0,len(path)-1):
            Tau_Matrix[path[i].adj_index][path[i+1].adj_index] =  Tau_Matrix[path[i].adj_index][path[i+1].adj_index] + delTau
        

def make_tour(nodelist,adj,Tau_Matrix): #make a tour for an ant
    for node in nodelist:
        node.discov = 0
    discov_count = 0
    current = choose_random_neighbour(nodelist) #choose random start city for kth ant
    current.discov = 1
    path = [current] #path of kth Ant
    while(discov_count <= len(nodelist)-2): #while nodes left
        neighbour = choose_random_neighbour(nodelist)
        probability = probab(current,neighbour,nodelist,adj,Tau_Matrix)
        # print("Pro",probability)

        if random.uniform(0,1) <= probability :
            neighbour.discov = 1
            discov_count += 1
            path.append(neighbour)
            current = neighbour
    return path
    






def Ant_Opt(nodelist,adj,Tau_Matrix,m_ants):    #get the best tour after all ants exhausted
    best_path = best(float('inf'),[None]*len(nodelist))

    kth_path = []
    for i in range(0,1):
        for i in range (0,m_ants):
            kth_path = make_tour(nodelist,adj,Tau_Matrix)   #make tour for kth ant
            if path_cost(kth_path,adj) < best_path.cost:    #update best path
                best_path.cost = path_cost(kth_path,adj)
                best_path.path = kth_path

            update_path_pheromones(kth_path,Tau_Matrix,adj)    # Update pheromones of each edge of this path after the tour
    
    return best_path














f = open(sys.argv[1],"r")

dist_type = f.readline().rstrip()
N = int(f.readline())

# print(dist_type,N)

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
for i in range(0,N): #making list of nodes/cities
    temp = node(coords[i][0],coords[i][1],0,i)
    nodelist[i] = temp

m_ants = 50

b = Ant_Opt(nodelist,adj,Tau_Matrix,m_ants)

print(b.cost)

for i in b.path:
    print(i.adj_index,end=" ")
# print(path_cost(nodelist,adj))







