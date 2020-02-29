import random
import math

import sys
from itertools import islice
from queue import PriorityQueue
import numpy as np


dist_matrix = []

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    for i in range(int(lines[1])+2, 2*int(lines[1])+2):
        dist_matrix.append([float(num) for num in lines[i].split(' ')])

Eval_list = []
solution_history = []


def GenPopulation(o):
    x = o.copy()
    random.shuffle(x)
    return x


def crossover(parent1, parent2):
    child = []

    rand1 = round(random.random() * len(parent1))
    rand2 = round(random.random() * len(parent2))

    firstDivider = min(rand1, rand2)
    secondDivider = max(rand1, rand2)

    for i in range(int(firstDivider), int(secondDivider)):
        child.append(parent1[i])
    for i in parent2:
        if i not in child:
            child.append(i)
    return child


def order_crossover(parent1, parent2):
    d = len(dist_matrix)
    start = random.randint(0, d - 2)
    end = random.randint(start, d - 1)
    child1 = parent1[start:end]
    child2 = parent2[start:end]
    for city in parent1:
        if city not in child2:
            child2.append(city)
    for city in parent2:
        if city not in child1:
            child1.append(city)
    return [child1, child2]


def Eval(sol):
    sum = 0.0
    for i in range(0, len(sol)-1):
        sum += dist_matrix[sol[i]][sol[i+1]]
    sum += dist_matrix[sol[0]][sol[99]]
    return sum


def GeneticAlgorithm():
    population_size = 100
    k = random.randint(0, population_size/2)
    population = PriorityQueue()
    # population_eval = []
    temp_population = []
    node = []
    for i in range(0, len(dist_matrix)):
        node.append(i)
    temp_population.append(node)
    for i in range(0, population_size):
        a = GenPopulation(node)
        if a not in temp_population:
            temp_population.append(a)
            population.put((-1*Eval(a), a))
        else:
            i -= 1
    count = 0
    while count < 100:
        count = count + 1
        temp_children = []
        children = PriorityQueue()
        foo = int(population_size/2)
        for i in range(0, foo):
            s = order_crossover(temp_population[i], temp_population[i+1])
            if s[0] not in temp_children:
                temp_children.append(s[0])
                children.put((Eval(s[0]), s[0]))
            if s[1] not in temp_children:
                temp_children.append(s[1])
                children.put((Eval(s[1]), s[1]))
            else:
                i = i - 1
        # min = 100000
        m = k
        while m > 0:
            s = children.get()
            # z = population.get()
            population.put((-1*s[0], s[1]))
            m = m - 1
    while not population.empty():
        sol = population.get()
    return sol


temp = 100000
gasolution = GeneticAlgorithm()
ff = open("Output_Genetic.txt", 'w')
ff.write(str(-1*gasolution[0]))
ff.write("\n")
ff.write(" ".join(list(map(str, gasolution[1]))))
ff.write("\n")
ff.close()
