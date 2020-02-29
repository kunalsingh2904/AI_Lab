import random
import sys
import random
import math
import numpy as np


class TravellingSalesman():

    def __init__(self, input_file):
        with open(input_file) as fp:
            lines = fp.readlines()
            self.num_of_cities = int(lines[1])

            self.cities = []
            for line in lines[2:self.num_of_cities + 2]:
                city = line.strip().split(' ')
                self.cities.append(tuple(city))

            self.distance_matrix = []
            for dist in lines[self.num_of_cities + 2:]:
                distance = dist.strip().split(' ')
                self.distance_matrix.append([float(x) for x in distance])

    def random_tour(self):
        tour = list(range(self.num_of_cities))
        random.shuffle(tour)
        return tour

    def eval(self, tour):
        cost = 0
        for i in range(self.num_of_cities):
            cost += self.distance_matrix[tour[i]
                                         ][tour[(i+1) % self.num_of_cities]]
        return cost

    def random_neighbour(self, tour):
        """
        Two city exchange
        """
        new_tour = tour.copy()
        random_city = random.sample(range(self.num_of_cities), 2)
        new_tour[random_city[0]], new_tour[random_city[1]
                                           ] = tour[random_city[1]], tour[random_city[0]]
        return new_tour

    def print_tour(self, tour):
        with open('Output_Simulated.txt', "w") as f:
            f.write(str(self.eval(tour)))
            f.write("\n")
            for city in tour:
                f.write(str(self.cities.index(
                    tuple((self.cities[city][0], self.cities[city][1])))))
                f.write(" ")
            f.write("\n")


class SimulatedAnnealing(TravellingSalesman):
    def __init__(self, input_file):
        super().__init__(input_file)

    def cooling(self, temperature, time, func_type=1):
        if func_type == 1:
            return temperature / 10
        if func_type == 2:
            return temperature / (time + 1)
        if func_type == 3:
            return temperature / ((time + 1) ** 2)
        if func_type == 4:
            return (temperature) / ((1001 - time))
            # return (temperature) / ((1 + np.log(1+time)))
        if func_type == 5:
            return temperature - (time * 10)

    def simulated_annealing(self):
        tour = self.random_tour()
        best_tour = tour
        temperature = 10000
        num_of_epochs = 1000
        for time in range(num_of_epochs):
            while temperature > 1.00000000022e-300:
                neighbour = self.random_neighbour(tour)
                delta_eval = self.eval(neighbour) - self.eval(tour)
                if random.uniform(0, 1) < sigmoid(delta_eval / temperature):
                    tour = neighbour
                    if self.eval(tour) < self.eval(best_tour):
                        best_tour = tour
                    temperature = self.cooling(temperature, time, func_type=4)
                    break
        return best_tour


def sigmoid(x):
    np.seterr(over='ignore')
    return 1 / (1 + np.exp(x))


def main():
    tsp = SimulatedAnnealing(sys.argv[1])
    tour = tsp.simulated_annealing()
    tsp.print_tour(tour)


if __name__ == "__main__":
    main()
