import sys
# import numpy as np


class node:
    """[Node for each vertex in graph.]
        Each node have heuristic value: data, mark and solved and list of child
    """

    def __init__(self):
        """[constructor for class node]
        """
        self.data = None
        self.mark = None
        self.solved = None
        self.v = list(list())


# edge cost for graph
edge_cost = 0


def insert(root):
    """[Insert node in graph based on And-Or condition]

    Arguments:
        root {[node]} -- [root is starting node of problem]
    """
    root.data = int(input("Enter data of node : "))
    # taking input as number of child
    print("Enter number of sets for value ", root.data, " :")
    or_no = int(input())
    for i in range(or_no):
        ans = list()
        # Taking no of and node as input
        print("Enter number of AND nodes for branch no.",
              i+1, " of ", root.data, ":")
        and_no = int(input())
        for _ in range(and_no):
            n = node()
            n.solved = False        # initializing solved as False
            n.mark = False          # initializing Mark as False
            # Taking child for this node
            insert(n)
            ans.append(n)
        root.v.append(ans)


def aostar(root):
    """[AO star algorithm]

    Arguments:
        root {[node]} -- [algorithm will start searching from root node]
    """
    min_ans = [root]
    while(not root.solved):     # Searching start with root
        next_node = root
        st = list()
        while (next_node and next_node.mark):   # checking its mark
            if len(next_node.v) == 0:
                root.solved = True
                return
            cost = float('inf')
            st.append(next_node)
            for i in range(len(next_node.v)):
                ans = next_node.v[i]
                ans_v = ans[:]
                temp_cost = 0
                for j in range(len(ans_v)):
                    n = ans_v[j]
                    temp_cost += n.data     # updating heuristic
                if temp_cost < cost:        # comparing heuristic to update
                    min_ans = ans
                    cost = temp_cost
            min_ans_v = min_ans
            next_node = None
            for j in range(len(min_ans_v)):
                if min_ans_v[j].mark:       # checking mark of child
                    next_node = min_ans_v[j]
                    break

        # copying list of node to explore further
        min_ans_v = min_ans[:]
        for j in range(len(min_ans_v)):
            n = min_ans_v[j]
            print("Exploring: ", n.data)
            final_cost = float('inf')
            if len(n.v) == 0:       # leaf node
                n.mark = True
            else:
                for i in range(len(n.v)):
                    # print("------", len(n.v))
                    ans = n.v[i]
                    ans_v = ans[:]
                    temp_cost = 0
                    for j in range(len(ans_v)):
                        nn = ans_v[j]
                        temp_cost += nn.data        # updating heuristic
                        temp_cost += edge_cost      # adding edge cost to heuristic of parent
                    if temp_cost < final_cost:
                        final_cost = temp_cost
                n.data = final_cost
                n.mark = True       # mark the explored node
            print("Marked: ", n.data)
        for i in range(20):
            print("=", end="")
        print()
        while(st):          # reassigning heuristic of all node in path
            n = st[0]
            print(n.data, " ")
            st.pop(0)               # taking top node
            final_cost = float('inf')
            for i in range(len(n.v)):
                ans = n.v[i]
                ans_v = ans.copy()
                temp_cost = 0
                for j in range(len(ans_v)):
                    nn = ans_v[j]
                    temp_cost += nn.data        # updating heuristic
                    temp_cost += edge_cost      # adding edge cost to heuristic of parent
                # comparing new heuristic to update
                if temp_cost < final_cost:
                    min_ans = ans
                    final_cost = temp_cost
            n.data = final_cost
        print()
        next_node = root


def printgraph(root):
    """[print graph pre-order traversal]

    Arguments:
        root {[node]} -- [start with root node and print all child following pre-order traversal]
        (print-->left-->right)
    """
    if root:
        print(root.data, " ")
        vec = root.v
        for i in range(len(vec)):
            ans = root.v[i]
            ans_v = ans.copy()
            for j in range(len(ans_v)):
                n = ans_v[j]
                printgraph(n)
    return


if __name__ == '__main__':      # main function
    root = node()       # initial node==> root
    root.solved = False
    root.mark = False
    insert(root)        # taking input of graph
    print()
    edge_cost = int(input("Enter the edge cost: "))  # taking edge cost
    print("the tree is as follows:")
    printgraph(root)        # printing graph
    print()
    aostar(root)        # calling ao* star algorithm
    # printing minimum heuristic of root(updated finally)
    print("The minimum cost is: ", root.data)
