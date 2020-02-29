import sys
import random
import math
import numpy as np
from TravellingSalesman import TravellingSalesman


def sigmoid(x: float):
    np.seterr(over='ignore')
    return 1 / (1 + np.exp(x))


class SimulatedAnnealing(TravellingSalesman):

    def __init__(self, input_file):
        super().__init__(input_file)

    def cooling(self, temperature, time, func_type=1):
        """
        Defines different types of cooling functions
        `func_type` decides which function to use
        """
        if func_type == 1:
            return temperature / 10
        if func_type == 2:
            return temperature / ((time + 1))
        if func_type == 3:
            return temperature - (time ** 2)
        if func_type == 4:
            return temperature - 10
    
    def simulated_annealing(self):

        tour = self.random_tour()
        best_tour = tour
        temperature = self.num_of_cities ** 2
        self.num_of_epochs = 1000
        for time in range(self.num_of_epochs):
            for _ in range(1000):
                if temperature < 0.000009e-300:
                    break
                neighbour = self.random_neighbour(tour)
                delta_eval = self.eval(neighbour) - self.eval(tour)
                if random.uniform(0, 1) < sigmoid(delta_eval / temperature):
                    tour = neighbour
                    if self.eval(tour) < self.eval(best_tour):
                        best_tour = tour
                    temperature = self.cooling(temperature, time, func_type=3)
                    print(temperature)

        return best_tour


def main():
    tsp = SimulatedAnnealing(sys.argv[1])
    tour = tsp.simulated_annealing()
    tsp.print_tour(tour)


if __name__ == "__main__":
    main()
