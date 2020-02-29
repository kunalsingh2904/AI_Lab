import random
import sys              # Importing required library
import numpy as np


class SimulatedAnnealing():
    def __init__(self, input_file):   # constructor
        with open(input_file) as fp:        # opening file
            lines = fp.readlines()          # reading lines
            self.num_of_cities = int(lines[1])      # no of cities

            self.cities = []        # storing cities
            for line in lines[2:self.num_of_cities + 2]:
                city = line.strip().split(' ')
                self.cities.append(tuple(city))     # storing coordinates

            self.distance_matrix = []       # distance matrix
            for dist in lines[self.num_of_cities + 2:]:
                distance = dist.strip().split(' ')
                self.distance_matrix.append(
                    [float(x) for x in distance])       # storing values

    def random_tour(self):
        tour = list(range(self.num_of_cities))      # creating tour list
        random.shuffle(tour)        # randoming the index
        return tour     # return random list

    def eval(self, tour):
        cost = 0        # cost
        for i in range(self.num_of_cities):     # calculating cost
            cost += self.distance_matrix[tour[i]
                                         ][tour[(i+1) % self.num_of_cities]]        # updating cost
        return cost         # return Total cost

    def random_neighbour(self, tour):
        new_tour = tour.copy()      # copying tour in temporary list
        # returns a particular length list of items chosen from the sequence
        random_city = random.sample(range(self.num_of_cities), 2)
        new_tour[random_city[0]], new_tour[random_city[1]
                                           ] = tour[random_city[1]], tour[random_city[0]]  # Updating
        return new_tour     # returning new tour

    def print_tour(self, tour):
        # with open('Output_Simulated.txt', "w") as f:      # writing desired output in file
        #     f.write(str(self.eval(tour)))
        #     f.write("\n")
        #     for city in tour:
                # f.write(str(self.cities.index(
                #     tuple((self.cities[city][0], self.cities[city][1])))))
        #         f.write(" ")
        #     f.write("\n")

        print(self.eval(tour))      # Print Cost
        for city in tour:           # print path index
            print(self.cities.index(
                tuple((self.cities[city][0], self.cities[city][1]))), end=" ")
        print()

    def cooling(self, temperature, time, func_type=1):      # cooling function
        if func_type == 1:
            return temperature / 10         # type 1
        if func_type == 2:
            return temperature / (time + 1)             # type 2
        if func_type == 3:
            return temperature / ((time + 1) ** 2)          # type 3
        if func_type == 4:
            return (temperature) / ((1001 - time))          # type 4
        if func_type == 5:
            return temperature - (time * 10)                # type 5

    def simulated_annealing(self):              # Main Algorithm
        tour = self.random_tour()           # random index list
        best_tour = tour        # initialization
        temperature = 10000             # starting temprature
        num_of_epochs = 1000  # No of epochs
        for time in range(num_of_epochs):       # Running no of epoch time
            while temperature > 1.00000000022e-300:     # termination criteria
                neighbour = self.random_neighbour(
                    tour)   # new random index list
                delta_eval = self.eval(neighbour) - \
                    self.eval(tour)               # cost difference
                if random.uniform(0, 1) < sigmoid(delta_eval / temperature):
                    tour = neighbour                # updating tour
                    if self.eval(tour) < self.eval(best_tour):
                        best_tour = tour        # taking best tour
                    temperature = self.cooling(
                        temperature, time, func_type=5)      # cooling temprature
                    break
        return best_tour        # Done


def sigmoid(x):         # sigmoid function(increasing)
    np.seterr(over='ignore')        # ignore error
    return 1 / (1 + np.exp(x))  # function


tsp = SimulatedAnnealing(sys.argv[1])       # calling constructor
tour = tsp.simulated_annealing()        # Best tour
tsp.print_tour(tour)            # printing
