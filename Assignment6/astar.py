import sys
import numpy as np


class node:
    def __init__(self):
        self.data = None
        self.mark = None
        self.solved = None
        self.v = list(list())


edge_cost = 0


def insert(root):
    root.data = int(input("Enter data of node : "))
    # or_no = None
    print("Enter number of nodes for value ", root.data, " :")
    or_no = int(input())
    for i in range(or_no):
        ans = list()
        # and_no = None
        print("Enter number of AND nodes for", i+1, root.data, ":")
        and_no = int(input())
        for _ in range(and_no):
            n = node()
            n.solved = False
            n.mark = False
            insert(n)
            ans.append(n)
        root.v.append(ans)


def aostar(root):
    min_ans = [root]
    while(not root.solved):
        next_node = root
        st = list()
        while (next_node and next_node.mark):
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
                    temp_cost += n.data
                if temp_cost < cost:
                    min_ans = ans
                    cost = temp_cost
            min_ans_v = min_ans
            next_node = None
            for j in range(len(min_ans_v)):
                if min_ans_v[j].mark:
                    next_node = min_ans_v[j]
                    break
                # line 79

        min_ans_v = min_ans[:]
        for j in range(len(min_ans_v)):
            n = min_ans_v[j]
            print("Exploring: ", n.data)
            final_cost = float('inf')
            if len(n.v) == 0:
                n.mark = True
            else:
                for i in range(len(n.v)):
                    # print("------", len(n.v))
                    ans = n.v[i]
                    ans_v = ans[:]
                    temp_cost = 0
                    for j in range(len(ans_v)):
                        nn = ans_v[j]
                        temp_cost += nn.data
                        temp_cost += edge_cost
                    if temp_cost < final_cost:
                        final_cost = temp_cost
                n.data = final_cost
                n.mark = True
            print("Marked: ", n.data)

        # line 118
        for i in range(20):
            print("=", end="")
        print()
        while(st):
            n = st[0]
            print(n.data, " ")
            st.pop(0)
            final_cost = float('inf')
            for i in range(len(n.v)):
                ans = n.v[i]
                ans_v = ans.copy()
                temp_cost = 0
                for j in range(len(ans_v)):
                    nn = ans_v[j]
                    temp_cost += nn.data
                    temp_cost += edge_cost
                if temp_cost < final_cost:
                    min_ans = ans
                    final_cost = temp_cost
            n.data = final_cost
        print()
        next_node = root


def printgraph(root):
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


if __name__ == '__main__':
    root = node()
    root.solved = False
    root.mark = False
    insert(root)
    print()
    edge_cost = int(input("Enter the edge cost: "))
    print("the tree is as follows:")
    printgraph(root)
    print()
    aostar(root)
    print("The minimum cost is: ", root.data)
