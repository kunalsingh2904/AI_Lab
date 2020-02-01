import sys
import math as m


f = open(sys.argv[1],"r")

dist_type = f.readline()
N = int(f.readline())

print(dist_type,N)

coords = [[None]*2]*N
adj = [[None]*N]*N

for i in range(0,N):
    coords[i] = list(map(lambda x: float(x), list(f.readline().rstrip().split(" "))))
for i in range(0,N):
    adj[i] = list(map(lambda x: float(x), list(f.readline().rstrip().split(" "))))

for i in range(0,N):
    print(coords[i])

for i in range(0,N):
    print(adj[i])
delE = 13
T = 10
print(  1/(1+ m.exp( (delE)/T  ) )    )