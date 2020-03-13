# AO\* algorithm group 5

data = h(n)
sets = count of individal OR nodes + joint AND nodes are counted as 1
The Data input follows a Pre_Order Traversal
Types of prompts:
Enter data of node --> Enter h(n)
Enter number of sets for value 'data_value' --> Enter no. OR nodes + joint AND nodes

## Example1 in Report: Overestimate

![Eg1: Overestimate](pics/overstimates.png)

### Run as : python3 ao_star.py

### inputs:

Prompt: Enter data of node : 3
Prompt: Enter number of sets for value 3 :
Input: 1
Prompt: Enter number of AND nodes for branch no. 1 of 3 :
Input: 2
Prompt: Enter data of node : 5
Prompt: Enter number of sets for value 5 :
Input: 2
Prompt: Enter number of AND nodes for branch no. 1 of 5 :
Input: 1
Prompt: Enter data of node : 7
Prompt: Enter number of sets for value 7 :
Input: 1
Prompt: Enter number of AND nodes for branch no. 1 of 7 :
Input: 2
Prompt: Enter data of node : 6
Prompt: Enter number of sets for value 6 :
Input: 0
Prompt: Enter data of node : 9
Prompt: Enter number of sets for value 9 :
Input: 0
Prompt: Enter number of AND nodes for branch no. 2 of 5 :
Input: 1
Prompt: Enter data of node : 6
Prompt: Enter number of sets for value 6 :
Input: 1
Prompt: Enter number of AND nodes for branch no. 1 of 6 :
Input: 2
Prompt: Enter data of node : 6
Prompt: Enter number of sets for value 6 :
Input: 0
Prompt: Enter data of node : 7
Prompt: Enter number of sets for value 7 :
Input: 0
Prompt: Enter data of node : 2
Prompt: Enter number of sets for value 2 :
Input: 2
Prompt: Enter number of AND nodes for branch no. 1 of 2 :
Input: 1
Prompt: Enter data of node : 4
Prompt: Enter number of sets for value 4 :
Input: 0
Prompt: Enter number of AND nodes for branch no. 2 of 2 :
Input: 1
Prompt: Enter data of node : 5
Prompt: Enter number of sets for value 5 :
Input: 0

Prompt: Enter the edge cost:
Input: 2

### Outputs:

the tree is as follows:
3  
5  
7  
6  
9  
6  
6  
7  
2  
4  
5

Exploring: 3
Marked: 11
====================

Exploring: 5
Marked: 8
Exploring: 2
Marked: 6
====================
11

Exploring: 6
Marked: 17
====================
18  
8

Exploring: 7
Marked: 19
====================
18  
9

Exploring: 6
Marked: 6
Exploring: 7
Marked: 7
====================
19  
19  
17

The minimum cost is: 29

## Example 2: UnderEstimate

![Eg1: Overestimate](pics/underestimates.png)

### Run as : python3 ao_star.py

### inputs:

Prompt: Enter data of node : 1
Prompt: Enter number of sets for value 1 :
Input: 1
Prompt: Enter number of AND nodes for branch no. 1 of 1 :
Input: 2
Prompt: Enter data of node : 0
Prompt: Enter number of sets for value 0 :
Input: 2
Prompt: Enter number of AND nodes for branch no. 1 of 0 :
Input: 1
Prompt: Enter data of node : 2
Prompt: Enter number of sets for value 2 :
Input: 1
Prompt: Enter number of AND nodes for branch no. 1 of 2 :
Input: 2
Prompt: Enter data of node : 3
Prompt: Enter number of sets for value 3 :
Input: 0
Prompt: Enter data of node : 4
Prompt: Enter number of sets for value 4 :
Input: 0
Prompt: Enter number of AND nodes for branch no. 2 of 0 :
Input: 1
Prompt: Enter data of node : 1
Prompt: Enter number of sets for value 1 :
Input: 1
Prompt: Enter number of AND nodes for branch no. 1 of 1 :
Input: 2
Prompt: Enter data of node : 4
Prompt: Enter number of sets for value 4 :
Input: 0
Prompt: Enter data of node : 5
Prompt: Enter number of sets for value 5 :
Input: 0
Prompt: Enter data of node : 2
Prompt: Enter number of sets for value 2 :
Input: 2
Prompt: Enter number of AND nodes for branch no. 1 of 2 :
Input: 1
Prompt: Enter data of node : 3
Prompt: Enter number of sets for value 3 :
Input: 0
Prompt: Enter number of AND nodes for branch no. 2 of 2 :
Input: 1
Prompt: Enter data of node : 1
Prompt: Enter number of sets for value 1 :
Input: 0

Prompt: Enter the edge cost:
Input: 2

### Outputs:

the tree is as follows:
1  
0  
2  
3  
4  
1  
4  
5  
2  
3  
1

Exploring: 1
Marked: 6
====================

Exploring: 0
Marked: 3
Exploring: 2
Marked: 3
====================
6

Exploring: 1
Marked: 13
====================
10  
3

Exploring: 2
Marked: 11
====================
10  
4

Exploring: 3
Marked: 3
Exploring: 4
Marked: 4
====================
11  
13  
11

The minimum cost is: 20
