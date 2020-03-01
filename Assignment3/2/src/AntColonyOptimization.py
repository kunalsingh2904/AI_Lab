import sys
import random
from TravellingSalesman import TravellingSalesman


class Ant:

    def __init__(self, start_city, num_of_cities):
        """
        Initializes a new ant
        start_city is randomized for each ant
        """
        start_city = random.randint(0, num_of_cities - 1)
        self.to_visit = list(range(num_of_cities))
        self.to_visit.remove(start_city)
        self.tour = [start_city]

    def construct_tour(self, pheromone_matrix, distance_matrix):
        """
        Constructs a tour for a ant give the pheromone_matrix and distance_matrix
        """
        alpha = 100
        beta = 100
        current_city = self.tour[-1]
        while len(self.to_visit) != 0:
            prob_to_vist = []
            for next_city in self.to_visit:
                prob_to_vist.append((pheromone_matrix[current_city][next_city] ** alpha) +
                                    ((1 / distance_matrix[current_city][next_city]) ** beta))
            denominator_sum = sum(prob_to_vist)
            prob_to_vist = [prob / denominator_sum for prob in prob_to_vist]

            current_city = random.choices(self.to_visit, prob_to_vist, k=1)
            current_city = current_city[0]
            self.tour.append(current_city)
            self.to_visit.remove(current_city)


class AntColony(TravellingSalesman):

    def __init__(self, input_file):
        super().__init__(input_file)
        self.pheromone_matrix = [[0.1] * self.num_of_cities
                                 for _ in range(self.num_of_cities)]
        self.num_of_ants = 20
        self.pheromone_evapouration = 0.2
        self.Q = 1

    def ant_colony(self):
        best_tour = None
        for _ in range(1000):
            ants = [Ant(0, self.num_of_cities)] * self.num_of_ants
            pheromone_changes = [[0] * self.num_of_cities
                                 for _ in range(self.num_of_cities)]
            for ant in ants:
                ant.construct_tour(self.pheromone_matrix, self.distance_matrix)
                tour_cost = self.eval(ant.tour)
                if best_tour is None or tour_cost < self.eval(best_tour):
                    best_tour = ant.tour

                for i in range(self.num_of_cities):
                    pheromone_changes[ant.tour[i]][ant.tour[(i+1) % self.num_of_cities]] += self.Q / tour_cost

            for i in range(self.num_of_cities):
                self.pheromone_matrix[i] = [(1 - self.pheromone_evapouration) * old + change
                                            for old, change in zip(self.pheromone_matrix[i], pheromone_changes[i])]
        return best_tour


def main():
    tsp = AntColony(sys.argv[1])
    tour = tsp.ant_colony()
    tsp.print_tour(tour)


if __name__ == "__main__":
    main()
