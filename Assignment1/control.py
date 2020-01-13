import sys
import os

file = open(sys.argv[1], "r")
types = file.read(1)
types = int(types[0])
file.close()

if types == 0:   # bfs
    os.system("python  bfs.py " + sys.argv[1])
elif types == 1:  # dfs
    os.system("python  dfs.py " + sys.argv[1])
elif types == 2:  # dfid
    os.system("python  dfid.py " + sys.argv[1])
